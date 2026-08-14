"""
Fast numpy-only evaluator for the Final Eligibility module, used by the GA.

scikit-fuzzy's ControlSystem is convenient for one-off evaluation but too
slow to call thousands of times inside a GA fitness loop. This module
reimplements the SAME rule logic as final_eligibility.py, but:
  1. Precomputes each sample's rule firing strengths ONCE (they don't
     depend on the output boundaries being optimized).
  2. Re-runs only aggregation + centroid defuzzification per candidate,
     a handful of numpy operations. This keeps a full GA run to seconds.
"""
import numpy as np
import skfuzzy as fuzz

from app.fuzzy_engine.config import ACADEMIC_STRENGTH, NEED_SCORE, ACHIEVEMENT_SCORE
from app.fuzzy_engine.academic import evaluate_academic
from app.fuzzy_engine.need import evaluate_need
from app.fuzzy_engine.achievement import evaluate_achievement

FINAL_TIERS = ["Not Eligible", "Low Priority", "Medium Priority", "High Priority", "Highly Recommended"]
ACADEMIC_TO_FINAL = {
    "Poor": "Not Eligible", "Average": "Low Priority",
    "Good": "Medium Priority", "Excellent": "High Priority",
}
ELIGIBILITY_UNIVERSE = np.arange(0, 101, 1)


def _tier_up(cat, steps=1):
    idx = min(FINAL_TIERS.index(cat) + steps, len(FINAL_TIERS) - 1)
    return FINAL_TIERS[idx]


def _tier_down(cat, steps=1):
    idx = max(FINAL_TIERS.index(cat) - steps, 0)
    return FINAL_TIERS[idx]


def _degree_at(config, category, value, value_range):
    universe = np.arange(value_range[0], value_range[1] + 1, 1)
    points = config["categories"][category]
    mf = fuzz.trimf(universe, points) if len(points) == 3 else fuzz.trapmf(universe, points)
    return fuzz.interp_membership(universe, mf, value)


def precompute_rule_strengths(academic_score, need_score, achievement_score):
    """Same rules as final_eligibility.py's _build_rules, evaluated as scalars."""
    deg_academic = {c: _degree_at(ACADEMIC_STRENGTH, c, academic_score, ACADEMIC_STRENGTH["range"])
                     for c in ACADEMIC_STRENGTH["categories"]}
    deg_need = {c: _degree_at(NEED_SCORE, c, need_score, NEED_SCORE["range"])
                for c in NEED_SCORE["categories"]}
    deg_achievement = {c: _degree_at(ACHIEVEMENT_SCORE, c, achievement_score, ACHIEVEMENT_SCORE["range"])
                        for c in ACHIEVEMENT_SCORE["categories"]}

    strong_support = min(max(deg_need["High"], deg_need["Very High"]),
                          max(deg_achievement["Moderate"], deg_achievement["High"]))
    very_strong_support = min(deg_need["Very High"], deg_achievement["High"])
    weak_support = min(deg_need["Low"], deg_achievement["Low"])

    rules = []
    for academic_cat, base_final in ACADEMIC_TO_FINAL.items():
        a = deg_academic[academic_cat]
        rules.append((_tier_up(base_final, 2), min(a, very_strong_support)))
        rules.append((_tier_up(base_final, 1), min(a, 1 - very_strong_support, strong_support)))
        rules.append((_tier_down(base_final, 1), min(a, 1 - strong_support, weak_support)))
        rules.append((base_final, min(a, 1 - strong_support, 1 - weak_support)))

    rules.append(("Highly Recommended", min(deg_academic["Excellent"], deg_need["High"], deg_achievement["Moderate"])))
    rules.append(("Highly Recommended", min(deg_academic["Excellent"], deg_need["Very High"], deg_achievement["High"])))

    return rules


def decode_chromosome(genes):
    """13 genes -> the 5 Final Eligibility boundary lists, sorted, clipped to [0,100],
    and cast to plain Python floats (numpy scalars aren't JSON-serializable by FastAPI)."""
    g = np.clip(genes, 0, 100)
    g = [float(x) for x in g]
    return {
        "Not Eligible": sorted([0.0, 0.0, g[0], g[1]]),
        "Low Priority": sorted([g[2], g[3], g[4]]),
        "Medium Priority": sorted([g[5], g[6], g[7]]),
        "High Priority": sorted([g[8], g[9], g[10]]),
        "Highly Recommended": sorted([g[11], g[12], 100.0, 100.0]),
    }


def build_category_mfs(boundaries):
    mfs = {}
    for cat, points in boundaries.items():
        mfs[cat] = fuzz.trimf(ELIGIBILITY_UNIVERSE, points) if len(points) == 3 \
            else fuzz.trapmf(ELIGIBILITY_UNIVERSE, points)
    return mfs


def evaluate_with_boundaries(rule_strengths, boundaries):
    """Mamdani aggregation + centroid defuzzification for one sample."""
    category_mfs = build_category_mfs(boundaries)
    aggregate = np.zeros_like(ELIGIBILITY_UNIVERSE, dtype=float)

    for target_cat, strength in rule_strengths:
        if strength <= 0:
            continue
        aggregate = np.fmax(aggregate, np.fmin(strength, category_mfs[target_cat]))

    if aggregate.sum() == 0:
        return 0.0
    return float(fuzz.defuzz(ELIGIBILITY_UNIVERSE, aggregate, "centroid"))


def prepare_samples(sample_students):
    """Runs Modules 1-3 (unchanged) once per sample, then precomputes Module 4 rule strengths."""
    prepared = []
    for s in sample_students:
        cgpa_val = s["cgpa"] if s["semester"] >= 2 else None
        entrance_percent = (s["entrance_obtained"] / s["entrance_max"]) * 100

        academic_score, _ = evaluate_academic(s["marks_10th"], s["marks_12th"], entrance_percent, cgpa_val)
        need_score, _ = evaluate_need(s["annual_income"], s["disability"], s["hostel_type"], s["location"])
        achievement_score, _ = evaluate_achievement(s["extra_curricular"])

        rule_strengths = precompute_rule_strengths(academic_score, need_score, achievement_score)
        prepared.append({"label": s["label"], "ideal_score": s["ideal_score"], "rule_strengths": rule_strengths})
    return prepared