"""
Module 2: Financial & Social Need Fuzzy System.
Inputs: Annual Income, Disability, Hostel Type, Location.
Output: Need Score (0-100).
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

from app.fuzzy_engine.config import (
    ANNUAL_INCOME, DISABILITY, HOSTEL_TYPE, LOCATION, NEED_SCORE,
)

# Income alone spans the full input range with no gaps, so it alone
# guarantees rule coverage. Binary variables are NOT given standalone
# fallback rules — with crisp 0/1 inputs they'd fire at full strength
# and drown out income's (often partial) membership degree. Instead
# they only appear as modifiers inside combined rules below.
INCOME_TO_NEED = {
    "Very Low": "Very High",
    "Low": "High",
    "Medium": "Medium",
    "High": "Low",
}

NEED_TIERS = ["Low", "Medium", "High", "Very High"]


def _add_categories(fuzzy_var, config):
    for category, points in config["categories"].items():
        if len(points) == 3:
            fuzzy_var[category] = fuzz.trimf(fuzzy_var.universe, points)
        else:
            fuzzy_var[category] = fuzz.trapmf(fuzzy_var.universe, points)


def _build_variables():
    income = ctrl.Antecedent(np.arange(0, 1000001, 1000), "income")
    disability = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "disability")
    hostel = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "hostel")
    location = ctrl.Antecedent(np.arange(0, 1.01, 0.01), "location")
    need = ctrl.Consequent(np.arange(*NEED_SCORE["range"], 1), "need")

    _add_categories(income, ANNUAL_INCOME)
    _add_categories(disability, DISABILITY)
    _add_categories(hostel, HOSTEL_TYPE)
    _add_categories(location, LOCATION)
    _add_categories(need, NEED_SCORE)

    return income, disability, hostel, location, need


def _income_fallback_rules(income, need):
    """Guarantees full coverage on its own — income spans the whole universe."""
    return [ctrl.Rule(income[category], need[out]) for category, out in INCOME_TO_NEED.items()]


def _tier_up(category, steps=1):
    """Moves a Need category up by `steps` tiers, capped at 'Very High'."""
    idx = min(NEED_TIERS.index(category) + steps, len(NEED_TIERS) - 1)
    return NEED_TIERS[idx]


def _combined_rules(income, disability, hostel, location, need):
    """
    Expert-knowledge modifier rules: when disability, rural location, or
    hosteller status is present, need is bumped up one tier from whatever
    income alone would suggest. Multiple modifiers bump it up further.
    """
    modifier_present = disability["Yes"] | location["Rural"] | hostel["Hosteller"]
    strong_modifier = (disability["Yes"] & location["Rural"]) | (disability["Yes"] & hostel["Hosteller"])

    rules = []
    for category, base_need in INCOME_TO_NEED.items():
        rules.append(ctrl.Rule(income[category] & modifier_present, need[_tier_up(base_need, 1)]))
        rules.append(ctrl.Rule(income[category] & strong_modifier, need[_tier_up(base_need, 2)]))
    return rules


def _build_rules(income, disability, hostel, location, need):
    rules = []
    rules += _income_fallback_rules(income, need)
    rules += _combined_rules(income, disability, hostel, location, need)
    return rules


def evaluate_need(income_val, disability_bool, hostel_type_str, location_str):
    income, disability, hostel, location, need = _build_variables()
    rules = _build_rules(income, disability, hostel, location, need)

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    sim.input["income"] = income_val
    sim.input["disability"] = 1.0 if disability_bool else 0.0
    sim.input["hostel"] = 1.0 if hostel_type_str == "Hosteller" else 0.0
    sim.input["location"] = 1.0 if location_str == "Rural" else 0.0

    sim.compute()
    score = sim.output["need"]
    category = _score_to_category(score)
    return round(score, 2), category


def _score_to_category(score):
    if score < 35:
        return "Low"
    elif score < 55:
        return "Medium"
    elif score < 75:
        return "High"
    else:
        return "Very High"