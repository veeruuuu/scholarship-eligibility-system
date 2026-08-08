from app.fuzzy_engine.final_eligibility import evaluate_final

print("=== Final Eligibility Module Tests ===\n")

# Excellent academic + high need + good achievement -> Highly Recommended
score, rec = evaluate_final(90, 75, 70)
print(f"Excellent/HighNeed/Good: score={score}, recommendation={rec}")

# Poor everything -> Not Eligible
score, rec = evaluate_final(15, 10, 10)
print(f"Poor/Low/Low: score={score}, recommendation={rec}")

# Good academic, average need, moderate achievement
score, rec = evaluate_final(65, 50, 50)
print(f"Good/Medium/Moderate: score={score}, recommendation={rec}")

# High academic but low need, low achievement (well-off, strong student)
score, rec = evaluate_final(85, 15, 20)
print(f"Excellent/LowNeed/Low: score={score}, recommendation={rec}")

# Average academic, very high need, high achievement
score, rec = evaluate_final(45, 90, 85)
print(f"Average/VeryHighNeed/High: score={score}, recommendation={rec}")