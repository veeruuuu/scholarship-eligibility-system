from app.fuzzy_engine.academic import evaluate_academic

print("=== Academic Module Tests ===\n")

# Case 1: Very high academic scores, Semester 3 (CGPA included)
score, cat = evaluate_academic(95, 92, 88, cgpa_val=9.2)
print(f"High achiever (sem 3): score={score}, category={cat}")

# Case 2: Low academic scores, Semester 3
score, cat = evaluate_academic(40, 38, 35, cgpa_val=4.0)
print(f"Low achiever (sem 3): score={score}, category={cat}")

# Case 3: Semester 1 - CGPA must be excluded
score, cat = evaluate_academic(85, 82, 78, cgpa_val=None)
print(f"Average-good (sem 1, no CGPA): score={score}, category={cat}")

# Case 4: Mid-range everywhere
score, cat = evaluate_academic(65, 68, 62, cgpa_val=6.5)
print(f"Mid-range student: score={score}, category={cat}")