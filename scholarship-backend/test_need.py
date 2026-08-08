from app.fuzzy_engine.need import evaluate_need

print("=== Need Module Tests ===\n")

# Very low income + disability -> should be Very High need
score, cat = evaluate_need(40000, True, "Hosteller", "Rural")
print(f"Very low income + disability + hosteller + rural: score={score}, category={cat}")

# High income, urban, day scholar, no disability -> should be Low need
score, cat = evaluate_need(900000, False, "Day Scholar", "Urban")
print(f"High income + urban + day scholar: score={score}, category={cat}")

# Medium income, no other factors
score, cat = evaluate_need(400000, False, "Day Scholar", "Urban")
print(f"Medium income, no other need factors: score={score}, category={cat}")

# Low income, rural, no disability
score, cat = evaluate_need(150000, False, "Day Scholar", "Rural")
print(f"Low income + rural: score={score}, category={cat}")

# Disability=Yes only, otherwise comfortable
score, cat = evaluate_need(800000, True, "Day Scholar", "Urban")
print(f"High income but disability=Yes: score={score}, category={cat}")