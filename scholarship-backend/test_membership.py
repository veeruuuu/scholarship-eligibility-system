from app.fuzzy_engine.config import MARKS_10TH
from app.fuzzy_engine.membership import build_universe, build_membership

universe = build_universe(*MARKS_10TH["range"])

print("Testing 10th Marks membership functions\n")

for category, points in MARKS_10TH["categories"].items():
    mf = build_membership(universe, points)
    # Find the membership degree at mark = 78 as a sample check
    sample_mark = 78
    idx = int(sample_mark - MARKS_10TH["range"][0])
    degree = mf[idx]
    print(f"{category:15s} -> membership({sample_mark}) = {degree:.3f}")