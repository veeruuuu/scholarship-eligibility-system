from app.fuzzy_engine.achievement import evaluate_achievement

print("=== Achievement Module Tests ===\n")

for val in [0, 20, 40, 60, 85, 100]:
    score, cat = evaluate_achievement(val)
    print(f"Input={val:3d} -> score={score}, category={cat}")