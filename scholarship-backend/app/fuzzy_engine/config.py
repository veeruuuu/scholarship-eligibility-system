"""
Central configuration for all fuzzy membership function boundaries.
Each variable maps to a dict of {category_name: [points]}.
- 3 points -> triangular (a, b, c)
- 4 points -> trapezoidal (a, b, c, d)
"""

MARKS_10TH = {
    "range": [0, 100],
    "categories": {
        "Poor":          [0, 0, 35, 45],
        "Below Average": [35, 45, 50, 55],
        "Average":       [50, 55, 65, 70],
        "Good":          [65, 70, 80, 85],
        "Very Good":     [80, 85, 90, 95],
        "Excellent":     [90, 95, 100, 100],
    },
}

MARKS_12TH = {
    "range": [0, 100],
    "categories": {
        "Poor":          [0, 0, 35, 45],
        "Below Average": [35, 45, 50, 55],
        "Average":       [50, 55, 65, 70],
        "Good":          [65, 70, 80, 85],
        "Very Good":     [80, 85, 90, 95],
        "Excellent":     [90, 95, 100, 100],
    },
}

ENTRANCE_PERCENT = {
    "range": [0, 100],
    "categories": {
        "Poor":          [0, 0, 30, 40],
        "Below Average": [30, 40, 45, 50],
        "Average":       [45, 50, 60, 65],
        "Good":          [60, 65, 75, 80],
        "Very Good":     [75, 80, 88, 92],
        "Excellent":     [88, 92, 100, 100],
    },
}

# CGPA is only used from semester 2 onward. Triangular shapes here since
# CGPA is a tighter, more continuous scale (0-10) where a clear single
# "ideal point" per category is more natural than a plateau.
CGPA = {
    "range": [0, 10],
    "categories": {
        "Poor":      [0, 0, 5],
        "Average":   [4, 5.5, 7],
        "Good":      [6, 7.5, 9],
        "Excellent": [8, 10, 10],
    },
}

# Output of Module 1 (Academic Fuzzy System)
ACADEMIC_STRENGTH = {
    "range": [0, 100],
    "categories": {
        "Poor":      [0, 0, 20, 35],
        "Average":   [25, 40, 60],
        "Good":      [50, 65, 80],
        "Excellent": [70, 85, 100, 100],
    },
}

# Module 2 inputs

ANNUAL_INCOME = {
    "range": [0, 1000000],
    "categories": {
        "Very Low": [0, 0, 50000, 100000],
        "Low":      [50000, 100000, 200000, 300000],
        "Medium":   [200000, 300000, 500000, 700000],
        "High":     [500000, 700000, 1000000, 1000000],
    },
}

# Binary variables modeled as fuzzy on a [0,1] universe.
# 0 = No/Day Scholar/Urban, 1 = Yes/Hosteller/Rural.
DISABILITY = {
    "range": [0, 1],
    "categories": {
        "No":  [0, 0, 0, 0.5],
        "Yes": [0.5, 1, 1, 1],
    },
}

HOSTEL_TYPE = {
    "range": [0, 1],
    "categories": {
        "Day Scholar": [0, 0, 0, 0.5],
        "Hosteller":   [0.5, 1, 1, 1],
    },
}

LOCATION = {
    "range": [0, 1],
    "categories": {
        "Urban": [0, 0, 0, 0.5],
        "Rural": [0.5, 1, 1, 1],
    },
}

# Output of Module 2
NEED_SCORE = {
    "range": [0, 100],
    "categories": {
        "Low":       [0, 0, 20, 35],
        "Medium":    [25, 40, 60],
        "High":      [50, 65, 80],
        "Very High": [70, 85, 100, 100],
    },
}
# Module 3 input
EXTRA_CURRICULAR = {
    "range": [0, 100],
    "categories": {
        "None":      [0, 0, 10, 25],
        "Fair":      [15, 30, 45, 55],
        "Good":      [45, 55, 70, 80],
        "Excellent": [70, 80, 100, 100],
    },
}

# Output of Module 3
ACHIEVEMENT_SCORE = {
    "range": [0, 100],
    "categories": {
        "Low":       [0, 0, 25, 40],
        "Moderate":  [30, 50, 70],
        "High":      [60, 80, 100, 100],
    },
}

# Module 4 inputs mirror the outputs of Modules 1-3.
# Re-declared here (rather than reusing ACADEMIC_STRENGTH/NEED_SCORE/ACHIEVEMENT_SCORE
# directly) because Module 4 treats them as fresh Antecedents, not Consequents.
ACADEMIC_STRENGTH_IN = ACADEMIC_STRENGTH["categories"]
NEED_SCORE_IN = NEED_SCORE["categories"]
ACHIEVEMENT_SCORE_IN = ACHIEVEMENT_SCORE["categories"]

# Output of Module 4 — Final Eligibility (0-100)
FINAL_ELIGIBILITY = {
    "range": [0, 100],
    "categories": {
        "Not Eligible":       [0, 0, 15, 25],
        "Low Priority":       [15, 30, 45],
        "Medium Priority":    [35, 50, 65],
        "High Priority":      [55, 70, 85],
        "Highly Recommended": [75, 90, 100, 100],
    },
}