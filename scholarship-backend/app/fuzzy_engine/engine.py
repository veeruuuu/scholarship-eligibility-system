"""
Fuzzy Engine Facade.
The single entry point the API layer calls. Chains Modules 1-3 (Academic,
Need, Achievement) into Module 4 (Final), and packages a fully explainable
result. No fuzzy logic should live outside app/fuzzy_engine/ — this file
is the only bridge between the API and the fuzzy modules.
"""
from app.fuzzy_engine.academic import evaluate_academic
from app.fuzzy_engine.need import evaluate_need
from app.fuzzy_engine.achievement import evaluate_achievement
from app.fuzzy_engine.final_eligibility import evaluate_final


def run_evaluation(student):
    """
    student: a StudentInput pydantic model (or any object with matching attributes)
    Returns a plain dict with every field EvaluationResult needs.
    """
    # Module 1: Academic
    cgpa_val = student.cgpa if student.semester >= 2 else None
    entrance_percent = (student.entrance_obtained / student.entrance_max) * 100

    academic_score, academic_cat = evaluate_academic(
        student.marks_10th, student.marks_12th, entrance_percent, cgpa_val
    )

    # Module 2: Need
    need_score, need_cat = evaluate_need(
        student.annual_income, student.disability, student.hostel_type, student.location
    )

    # Module 3: Achievement
    achievement_score, achievement_cat = evaluate_achievement(student.extra_curricular)

    # Module 4: Final (consumes outputs of Modules 1-3)
    final_score, recommendation = evaluate_final(academic_score, need_score, achievement_score)

    key_factors = _build_key_factors(academic_cat, need_cat, achievement_cat)
    activated_rules = _build_activated_rules(academic_cat, need_cat, achievement_cat, recommendation)
    explanation = _build_explanation(
        academic_score, academic_cat, need_score, need_cat,
        achievement_score, achievement_cat, final_score, recommendation
    )

    return {
        "academic_strength": {"score": academic_score, "category": academic_cat},
        "need_score": {"score": need_score, "category": need_cat},
        "achievement_score": {"score": achievement_score, "category": achievement_cat},
        "final_eligibility": final_score,
        "recommendation": recommendation,
        "activated_rules": activated_rules,
        "key_factors": key_factors,
        "explanation": explanation,
    }


def _build_key_factors(academic_cat, need_cat, achievement_cat):
    factors = []
    factors.append(f"Academic performance is {academic_cat}")
    factors.append(f"Financial/social need is {need_cat}")
    factors.append(f"Extra-curricular achievement is {achievement_cat}")
    return factors


def _build_activated_rules(academic_cat, need_cat, achievement_cat, recommendation):
    """
    Describes, in plain terms, which category combination drove the result.
    This is a simplified summary (not a raw dump of every fuzzy rule that
    technically fired at some low degree) — kept readable for end users,
    per the explainability requirement.
    """
    return [
        f"IF Academic is {academic_cat} AND Need is {need_cat} AND Achievement is {achievement_cat} "
        f"THEN Eligibility is {recommendation}"
    ]


def _build_explanation(academic_score, academic_cat, need_score, need_cat,
                        achievement_score, achievement_cat, final_score, recommendation):
    return (
        f"The student's academic strength was rated {academic_cat} ({academic_score}/100), "
        f"their financial/social need was rated {need_cat} ({need_score}/100), and their "
        f"extra-curricular achievement was rated {achievement_cat} ({achievement_score}/100). "
        f"Combining these three factors through the fuzzy inference system produced a final "
        f"eligibility score of {final_score}/100, resulting in a recommendation of "
        f"'{recommendation}'."
    )