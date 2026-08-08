"""
Module 1: Academic Fuzzy System.
Inputs: 10th Marks, 12th Marks, Entrance %, CGPA (ignored for Semester 1).
Output: Academic Strength Score (0-100).
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

from app.fuzzy_engine.config import (
    MARKS_10TH, MARKS_12TH, ENTRANCE_PERCENT, CGPA, ACADEMIC_STRENGTH,
)

# Maps each input category down to the nearest output category.
# Used to build "fallback" single-condition rules that guarantee every
# input value activates at least one rule (prevents empty rule firing).
CATEGORY_TO_OUTPUT = {
    "Poor": "Poor",
    "Below Average": "Poor",
    "Average": "Average",
    "Good": "Good",
    "Very Good": "Good",
    "Excellent": "Excellent",
}


def _add_categories(fuzzy_var, config):
    for category, points in config["categories"].items():
        if len(points) == 3:
            fuzzy_var[category] = fuzz.trimf(fuzzy_var.universe, points)
        else:
            fuzzy_var[category] = fuzz.trapmf(fuzzy_var.universe, points)


def _build_variables(include_cgpa):
    marks10 = ctrl.Antecedent(np.arange(*MARKS_10TH["range"], 1), "marks10")
    marks12 = ctrl.Antecedent(np.arange(*MARKS_12TH["range"], 1), "marks12")
    entrance = ctrl.Antecedent(np.arange(*ENTRANCE_PERCENT["range"], 1), "entrance")
    academic_strength = ctrl.Consequent(np.arange(*ACADEMIC_STRENGTH["range"], 1), "academic_strength")

    _add_categories(marks10, MARKS_10TH)
    _add_categories(marks12, MARKS_12TH)
    _add_categories(entrance, ENTRANCE_PERCENT)
    _add_categories(academic_strength, ACADEMIC_STRENGTH)

    cgpa = None
    if include_cgpa:
        cgpa = ctrl.Antecedent(np.arange(0, 10.01, 0.1), "cgpa")
        _add_categories(cgpa, CGPA)

    return marks10, marks12, entrance, cgpa, academic_strength


def _fallback_rules(var, config, academic_strength):
    """
    One rule per category of a single variable, mapped to the nearest
    output category. Guarantees that ANY input value activates at least
    one rule for that variable alone, regardless of the other variables.
    These are intentionally 'weak' individual-input rules; the stronger
    combined rules below dominate the result when they also fire, since
    Mamdani aggregation takes the max across all activated output fuzzy sets.
    """
    rules = []
    for category in config["categories"]:
        output_cat = CATEGORY_TO_OUTPUT[category]
        rules.append(ctrl.Rule(var[category], academic_strength[output_cat]))
    return rules


def _combined_rules(marks10, marks12, entrance, cgpa, academic_strength):
    """
    Stronger, high-confidence rules representing expert knowledge:
    multiple inputs agreeing pushes the result more decisively.
    These add on top of (not replace) the fallback rules above.
    """
    rules = []

    if cgpa is not None:
        rules += [
            ctrl.Rule(marks10["Excellent"] & marks12["Excellent"] & entrance["Excellent"] & cgpa["Excellent"],
                      academic_strength["Excellent"]),
            ctrl.Rule((marks10["Excellent"] | marks10["Very Good"]) &
                      (marks12["Excellent"] | marks12["Very Good"]) &
                      (entrance["Excellent"] | entrance["Very Good"]) &
                      (cgpa["Excellent"] | cgpa["Good"]),
                      academic_strength["Excellent"]),
            ctrl.Rule((marks10["Good"] | marks10["Very Good"]) &
                      (marks12["Good"] | marks12["Very Good"]) &
                      (entrance["Good"] | entrance["Very Good"]) &
                      cgpa["Good"],
                      academic_strength["Good"]),
            ctrl.Rule(marks10["Average"] & marks12["Average"] & entrance["Average"] & cgpa["Average"],
                      academic_strength["Average"]),
            ctrl.Rule(marks10["Poor"] | marks12["Poor"] | entrance["Poor"] | cgpa["Poor"],
                      academic_strength["Poor"]),
        ]
    else:
        rules += [
            ctrl.Rule(marks10["Excellent"] & marks12["Excellent"] & entrance["Excellent"],
                      academic_strength["Excellent"]),
            ctrl.Rule((marks10["Excellent"] | marks10["Very Good"]) &
                      (marks12["Excellent"] | marks12["Very Good"]) &
                      (entrance["Excellent"] | entrance["Very Good"]),
                      academic_strength["Excellent"]),
            ctrl.Rule((marks10["Good"] | marks10["Very Good"]) &
                      (marks12["Good"] | marks12["Very Good"]) &
                      (entrance["Good"] | entrance["Very Good"]),
                      academic_strength["Good"]),
            ctrl.Rule(marks10["Average"] & marks12["Average"] & entrance["Average"],
                      academic_strength["Average"]),
            ctrl.Rule(marks10["Poor"] | marks12["Poor"] | entrance["Poor"],
                      academic_strength["Poor"]),
        ]

    return rules


def _build_rules(marks10, marks12, entrance, cgpa, academic_strength):
    rules = []
    rules += _fallback_rules(marks10, MARKS_10TH, academic_strength)
    rules += _fallback_rules(marks12, MARKS_12TH, academic_strength)
    rules += _fallback_rules(entrance, ENTRANCE_PERCENT, academic_strength)
    if cgpa is not None:
        rules += _fallback_rules(cgpa, CGPA, academic_strength)
    rules += _combined_rules(marks10, marks12, entrance, cgpa, academic_strength)
    return rules


def evaluate_academic(marks10_val, marks12_val, entrance_val, cgpa_val=None):
    include_cgpa = cgpa_val is not None

    marks10, marks12, entrance, cgpa, academic_strength = _build_variables(include_cgpa)
    rules = _build_rules(marks10, marks12, entrance, cgpa, academic_strength)

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    sim.input["marks10"] = marks10_val
    sim.input["marks12"] = marks12_val
    sim.input["entrance"] = entrance_val
    if include_cgpa:
        sim.input["cgpa"] = cgpa_val

    sim.compute()
    score = sim.output["academic_strength"]

    category = _score_to_category(score)
    return round(score, 2), category


def _score_to_category(score):
    if score < 35:
        return "Poor"
    elif score < 55:
        return "Average"
    elif score < 75:
        return "Good"
    else:
        return "Excellent"