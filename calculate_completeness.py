import csv

CSV_FILE = "candidate_compounds.csv"

EVIDENCE_FIELDS = [
    "source_database",
    "molecular_identifier",
    "target",
    "mechanism_of_action",
    "evidence_stage",
    "potency",
    "selectivity",
    "adme",
    "safety_toxicity",
    "supporting_publications"
]


def is_complete(value):
    if not value:
        return False

    value = value.strip()

    if value.upper() in [
        "UNKNOWN",
        "UNKNOWN / NOT FOUND",
        "NOT FOUND",
        "N/A"
    ]:
        return False

    return True


with open(CSV_FILE, newline="", encoding="utf-8-sig") as file:
    candidates = list(csv.DictReader(file))


print("\nTB Candidate Evidence Completeness")
print("=" * 50)

for candidate in candidates:

    completed = 0

    for field in EVIDENCE_FIELDS:
        if is_complete(candidate[field]):
            completed += 1

    total = len(EVIDENCE_FIELDS)
    percentage = (completed / total) * 100

    print(
        f"{candidate['candidate_id']} - "
        f"{candidate['compound_name']}: "
        f"{completed}/{total} fields = {percentage:.0f}%"
    )