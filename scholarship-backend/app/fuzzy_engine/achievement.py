"""
Module 3: Achievement Fuzzy System.
Input: Extra-Curricular Activity Score (0-100).
Output: Achievement Score (0-100).
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

from app.fuzzy_engine.config import EXTRA_CURRICULAR, ACHIEVEMENT_SCORE

# Direct 1:1 mapping since there's only one input — no rule explosion possible.
INPUT_TO_OUTPUT = {
    "None": "Low",
    "Fair": "Moderate",
    "Good": "Moderate",
    "Excellent": "High",
}


def _add_categories(fuzzy_var, config):
    for category, points in config["categories"].items():
        if len(points) == 3:
            fuzzy_var[category] = fuzz.trimf(fuzzy_var.universe, points)
        else:
            fuzzy_var[category] = fuzz.trapmf(fuzzy_var.universe, points)


def _build_variables():
    extra = ctrl.Antecedent(np.arange(*EXTRA_CURRICULAR["range"], 1), "extra")
    achievement = ctrl.Consequent(np.arange(*ACHIEVEMENT_SCORE["range"], 1), "achievement")

    _add_categories(extra, EXTRA_CURRICULAR)
    _add_categories(achievement, ACHIEVEMENT_SCORE)

    return extra, achievement


def _build_rules(extra, achievement):
    # Single input spans the full universe with no gaps -> full coverage guaranteed.
    return [ctrl.Rule(extra[category], achievement[out]) for category, out in INPUT_TO_OUTPUT.items()]


def evaluate_achievement(extra_curricular_val):
    """Returns: (score: float, category: str)"""
    extra, achievement = _build_variables()
    rules = _build_rules(extra, achievement)

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    sim.input["extra"] = extra_curricular_val
    sim.compute()

    score = sim.output["achievement"]
    category = _score_to_category(score)
    return round(score, 2), category


def _score_to_category(score):
    if score < 35:
        return "Low"
    elif score < 65:
        return "Moderate"
    else:
        return "High"