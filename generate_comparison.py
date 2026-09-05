import csv

CSV_FILE = "../candidate_compounds.csv"
OUTPUT_FILE = "candidate_comparison_results.csv"

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

results = []

for candidate in candidates:
    candidate_id = candidate["candidate_id"]

    if candidate_id not in SCORES:
        continue

    scores = SCORES[candidate_id]

    row = {
        "candidate_id": candidate_id,
        "compound_name": candidate["compound_name"],
    }

    for criterion, score in zip(CRITERIA, scores):
        row[criterion] = score

    row["total_score"] = sum(scores)

    results.append(row)

# Sort by highest score first
# Candidate ID is used as a tie-breaker.
results.sort(
    key=lambda x: (-x["total_score"], x["candidate_id"])
)

fieldnames = [
    "rank",
    "candidate_id",
    "compound_name"
] + CRITERIA + ["total_score"]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for rank, row in enumerate(results, start=1):
        output_row = {"rank": rank}
        output_row.update(row)
        writer.writerow(output_row)

print("\nFinal TB Candidate Ranking")
print("=" * 55)

for rank, row in enumerate(results, start=1):
    print(
        f"{rank}. {row['candidate_id']} - "
        f"{row['compound_name']}: "
        f"{row['total_score']}/40"
    )

print("\nComparison file created successfully:")
print(OUTPUT_FILE)