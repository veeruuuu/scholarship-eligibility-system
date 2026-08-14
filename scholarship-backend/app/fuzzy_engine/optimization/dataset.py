"""
Hand-labeled sample students for calibrating the Final Eligibility module.
`ideal_score` is the domain-expert's judgment of what the Final Eligibility
Score (0-100) SHOULD be for this student. REVIEW AND EDIT these before
running the GA — the optimizer is only as good as this target data.
"""

SAMPLE_STUDENTS = [
    {"label": "Excellent all-round, high need",
     "marks_10th": 95, "marks_12th": 93, "entrance_obtained": 170, "entrance_max": 180,
     "semester": 3, "cgpa": 9.3, "annual_income": 90000, "extra_curricular": 75,
     "disability": False, "hostel_type": "Hosteller", "location": "Rural", "ideal_score": 92},

    {"label": "Weak academics, comfortable income, no activity",
     "marks_10th": 38, "marks_12th": 35, "entrance_obtained": 60, "entrance_max": 180,
     "semester": 2, "cgpa": 3.5, "annual_income": 850000, "extra_curricular": 5,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 8},

    {"label": "Average student, average need",
     "marks_10th": 72, "marks_12th": 75, "entrance_obtained": 120, "entrance_max": 180,
     "semester": 4, "cgpa": 6.8, "annual_income": 350000, "extra_curricular": 50,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 52},

    {"label": "Strong student, well-off, low activity",
     "marks_10th": 94, "marks_12th": 96, "entrance_obtained": 165, "entrance_max": 180,
     "semester": 5, "cgpa": 9.0, "annual_income": 900000, "extra_curricular": 25,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 42},

    {"label": "Sem 1, decent marks, very low income, highly active",
     "marks_10th": 62, "marks_12th": 60, "entrance_obtained": 100, "entrance_max": 180,
     "semester": 1, "cgpa": None, "annual_income": 45000, "extra_curricular": 80,
     "disability": False, "hostel_type": "Hosteller", "location": "Rural", "ideal_score": 68},

    {"label": "Sem 1, good marks, moderate need",
     "marks_10th": 80, "marks_12th": 82, "entrance_obtained": 130, "entrance_max": 180,
     "semester": 1, "cgpa": None, "annual_income": 300000, "extra_curricular": 45,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 50},

    {"label": "Disability, very low income, average marks, no activity",
     "marks_10th": 65, "marks_12th": 63, "entrance_obtained": 105, "entrance_max": 180,
     "semester": 3, "cgpa": 6.5, "annual_income": 35000, "extra_curricular": 10,
     "disability": True, "hostel_type": "Hosteller", "location": "Rural", "ideal_score": 63},

    {"label": "High income, average marks, outstanding activity",
     "marks_10th": 68, "marks_12th": 70, "entrance_obtained": 115, "entrance_max": 180,
     "semester": 3, "cgpa": 6.9, "annual_income": 780000, "extra_curricular": 90,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 40},

    {"label": "Below-average marks, moderate income",
     "marks_10th": 48, "marks_12th": 50, "entrance_obtained": 80, "entrance_max": 180,
     "semester": 2, "cgpa": 4.8, "annual_income": 200000, "extra_curricular": 35,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 16},

    {"label": "Good marks, low income, outstanding activity",
     "marks_10th": 78, "marks_12th": 80, "entrance_obtained": 135, "entrance_max": 180,
     "semester": 4, "cgpa": 7.6, "annual_income": 60000, "extra_curricular": 88,
     "disability": False, "hostel_type": "Hosteller", "location": "Rural", "ideal_score": 79},

    {"label": "Sem 1, excellent marks, moderate need",
     "marks_10th": 92, "marks_12th": 90, "entrance_obtained": 160, "entrance_max": 180,
     "semester": 1, "cgpa": None, "annual_income": 280000, "extra_curricular": 55,
     "disability": False, "hostel_type": "Day Scholar", "location": "Urban", "ideal_score": 70},

    {"label": "Weak marks, disability, very low income, good activity",
     "marks_10th": 40, "marks_12th": 42, "entrance_obtained": 70, "entrance_max": 180,
     "semester": 3, "cgpa": 4.0, "annual_income": 40000, "extra_curricular": 65,
     "disability": True, "hostel_type": "Hosteller", "location": "Rural", "ideal_score": 36},
]