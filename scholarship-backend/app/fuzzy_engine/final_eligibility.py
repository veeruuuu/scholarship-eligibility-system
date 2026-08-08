"""
Module 4: Final Fuzzy System.
Inputs: Academic Strength, Need Score, Achievement Score (outputs of Modules 1-3).
Output: Final Eligibility Score (0-100) + Recommendation label.
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

from app.fuzzy_engine.config import (
    ACADEMIC_STRENGTH, NEED_SCORE, ACHIEVEMENT_SCORE, FINAL_ELIGIBILITY,
)

# Baseline Final Eligibility tier per Academic Strength category.
# Academic Strength alone spans the full universe -> guarantees coverage.
ACADEMIC_TO_FINAL = {
    "Poor": "Not Eligible",
    "Average": "Low Priority",
    "Good": "Medium Priority",
    "Excellent": "High Priority",
}

FINAL_TIERS = ["Not Eligible", "Low Priority", "Medium Priority", "High Priority", "Highly Recommended"]


def _add_categories(fuzzy_var, config):
    for category, points in config["categories"].items():
        if len(points) == 3:
            fuzzy_var[category] = fuzz.trimf(fuzzy_var.universe, points)
        else:
            fuzzy_var[category] = fuzz.trapmf(fuzzy_var.universe, points)


def _build_variables():
    academic = ctrl.Antecedent(np.arange(*ACADEMIC_STRENGTH["range"], 1), "academic")
    need = ctrl.Antecedent(np.arange(*NEED_SCORE["range"], 1), "need")
    achievement = ctrl.Antecedent(np.arange(*ACHIEVEMENT_SCORE["range"], 1), "achievement")
    eligibility = ctrl.Consequent(np.arange(*FINAL_ELIGIBILITY["range"], 1), "eligibility")

    _add_categories(academic, ACADEMIC_STRENGTH)
    _add_categories(need, NEED_SCORE)
    _add_categories(achievement, ACHIEVEMENT_SCORE)
    _add_categories(eligibility, FINAL_ELIGIBILITY)

    return academic, need, achievement, eligibility


def _tier_up(category, steps=1):
    idx = min(FINAL_TIERS.index(category) + steps, len(FINAL_TIERS) - 1)
    return FINAL_TIERS[idx]


def _tier_down(category, steps=1):
    idx = max(FINAL_TIERS.index(category) - steps, 0)
    return FINAL_TIERS[idx]


def _build_rules(academic, need, achievement, eligibility):
    """
    For each Academic Strength category, exactly ONE of the four branches
    below fires (mutual exclusivity via fuzzy NOT), instead of a baseline
    rule competing with a separate modifier rule. This avoids the
    twin-hump centroid problem where a baseline tier and a shifted tier
    activate simultaneously and average out to a false middle value.

    Precedence: very strong support > strong support > weak support > baseline.
    """
    rules = []

    for academic_cat, base_final in ACADEMIC_TO_FINAL.items():
        strong_support = (need["High"] | need["Very High"]) & (achievement["Moderate"] | achievement["High"])
        very_strong_support = need["Very High"] & achievement["High"]
        weak_support = need["Low"] & achievement["Low"]

        # Very strong: boost 2 tiers
        rules.append(ctrl.Rule(
            academic[academic_cat] & very_strong_support,
            eligibility[_tier_up(base_final, 2)]
        ))
        # Strong (but not very strong): boost 1 tier
        rules.append(ctrl.Rule(
            academic[academic_cat] & ~very_strong_support & strong_support,
            eligibility[_tier_up(base_final, 1)]
        ))
        # Weak (and not strong): drop 1 tier
        rules.append(ctrl.Rule(
            academic[academic_cat] & ~strong_support & weak_support,
            eligibility[_tier_down(base_final, 1)]
        ))
        # Neither strong nor weak: baseline, unmodified
        rules.append(ctrl.Rule(
            academic[academic_cat] & ~strong_support & ~weak_support,
            eligibility[base_final]
        ))

    return rules


def evaluate_final(academic_score, need_score, achievement_score):
    """
    Takes the three crisp module scores (0-100 each) and produces the
    Final Eligibility Score + Recommendation label.
    Returns: (score: float, recommendation: str)
    """
    academic, need, achievement, eligibility = _build_variables()
    rules = _build_rules(academic, need, achievement, eligibility)

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    sim.input["academic"] = academic_score
    sim.input["need"] = need_score
    sim.input["achievement"] = achievement_score

    sim.compute()
    score = sim.output["eligibility"]
    recommendation = _score_to_recommendation(score)
    return round(score, 2), recommendation


def _score_to_recommendation(score):
    if score < 20:
        return "Not Eligible"
    elif score < 40:
        return "Low Priority"
    elif score < 60:
        return "Medium Priority"
    elif score < 80:
        return "High Priority"
    else:
        return "Highly Recommended"