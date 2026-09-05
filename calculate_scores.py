import csv

CSV_FILE = "../candidate_compounds.csv"

CRITERIA = [
    "Target relevance",
    "Mechanism evidence",
    "Potency evidence",
    "Selectivity evidence",
    "ADME evidence",
    "Safety evidence",
    "Research/development evidence",
    "Evidence completeness"
]

# Scores are based on the strength of documented evidence.
# This is NOT a clinical recommendation.

SCORES = {
    "C-001": [5, 5, 1, 1, 5, 4, 5, 4],
    "C-002": [5, 5, 4, 2, 5, 3, 5, 5],
    "C-003": [5, 4, 1, 1, 5, 3, 5, 4],
    "C-004": [5, 5, 1, 1, 5, 3, 5, 4],
    "C-005": [5, 5, 3, 2, 5, 3, 5, 4],
    "C-006": [5, 4, 2, 2, 4, 3, 5, 4],
    "C-007": [5, 4, 2, 2, 4, 3, 5, 4],
    "C-008": [4, 5, 2, 2, 5, 3, 5, 4],
    "C-009": [4, 3, 2, 2, 3, 2, 5, 4],
    "C-010": [4, 4, 2, 2, 3, 2, 3, 4]
}

with open(CSV_FILE, newline="", encoding="utf-8-sig") as file:
    candidates = list(csv.DictReader(file))

print("\nTB Candidate Evidence Scoring")
print("=" * 70)

for candidate in candidates:
    candidate_id = candidate["candidate_id"]
    name = candidate["compound_name"]

    scores = SCORES.get(candidate_id)

    if scores is None:
        print(f"{candidate_id} - {name}: SCORE NOT AVAILABLE")
        continue

    total = sum(scores)

    print(f"\n{candidate_id} - {name}")
    print("-" * 50)

    for criterion, score in zip(CRITERIA, scores):
        print(f"{criterion}: {score}/5")

    print(f"TOTAL SCORE: {total}/40")