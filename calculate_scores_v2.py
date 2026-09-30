import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "candidate_records_with_provenance.json"
OUTPUT_FILE = BASE_DIR / "candidate_comparison_results_v2.json"

METHOD_VERSION = "1.0.0"

MAX_SCORE_PER_DIMENSION = 5
MAX_TOTAL_SCORE = 40

SCORE_FIELDS = [
    "target_relevance",
    "mechanism_evidence",
    "potency_evidence",
    "selectivity_evidence",
    "adme_evidence",
    "safety_evidence",
    "research_development_evidence",
    "evidence_completeness"
]


def load_records():
    if not INPUT_FILE.exists():
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        return []

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("ERROR: Input JSON must contain a list.")
            return []

        return data

    except json.JSONDecodeError as error:
        print(f"ERROR: Invalid JSON: {error}")
        return []


def normalize_score(value):
    if value is None:
        return None

    if isinstance(value, bool):
        return None

    try:
        score = int(value)
    except (TypeError, ValueError):
        return None

    if score < 0 or score > MAX_SCORE_PER_DIMENSION:
        return None

    return score


def calculate_score(record):
    score_inputs = record.get("score", {}).get(
        "score_inputs", {}
    )

    normalized_inputs = {}

    for field in SCORE_FIELDS:
        normalized_inputs[field] = normalize_score(
            score_inputs.get(field)
        )

    missing_inputs = [
        field
        for field in SCORE_FIELDS
        if normalized_inputs[field] is None
    ]

    if missing_inputs:
        return {
            "score_inputs": normalized_inputs,
            "total": None,
            "maximum": MAX_TOTAL_SCORE,
            "method_version": METHOD_VERSION,
            "missing_inputs": missing_inputs,
            "score_status": "INCOMPLETE"
        }

    total = sum(normalized_inputs.values())

    return {
        "score_inputs": normalized_inputs,
        "total": total,
        "maximum": MAX_TOTAL_SCORE,
        "method_version": METHOD_VERSION,
        "missing_inputs": [],
        "score_status": "COMPLETE"
    }


def create_comparison_results(records):
    results = []

    for record in records:
        candidate_id = record.get(
            "candidate_id",
            "UNKNOWN"
        )

        compound = record.get("compound", {})

        compound_name = compound.get(
            "name",
            "UNKNOWN"
        )

        calculated = calculate_score(record)

        results.append({
            "candidate_id": candidate_id,
            "compound_name": compound_name,
            "score": calculated
        })

    complete_results = [
        result
        for result in results
        if result["score"]["score_status"] == "COMPLETE"
    ]

    incomplete_results = [
        result
        for result in results
        if result["score"]["score_status"] != "COMPLETE"
    ]

    complete_results.sort(
        key=lambda result: (
            -result["score"]["total"],
            result["candidate_id"]
        )
    )

    incomplete_results.sort(
        key=lambda result: result["candidate_id"]
    )

    ranked_results = []

    rank = 1

    for result in complete_results:
        result["rank"] = rank
        ranked_results.append(result)
        rank += 1

    for result in incomplete_results:
        result["rank"] = None
        ranked_results.append(result)

    return ranked_results


def save_results(results):
    output = {
        "method_version": METHOD_VERSION,
        "maximum_score": MAX_TOTAL_SCORE,
        "scoring_dimensions": SCORE_FIELDS,
        "results": results
    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            output,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(f"Saved: {OUTPUT_FILE.name}")


def test_score_normalization():
    print()
    print("Test 1: Score Normalization")
    print("=" * 50)

    passed = (
        normalize_score(0) == 0
        and normalize_score(3) == 3
        and normalize_score(5) == 5
        and normalize_score(6) is None
        and normalize_score(-1) is None
        and normalize_score(None) is None
    )

    print("Result: PASS" if passed else "Result: FAIL")

    return passed


def test_complete_score():
    print()
    print("Test 2: Complete Score")
    print("=" * 50)

    record = {
        "candidate_id": "TEST-001",
        "compound": {
            "name": "Test Compound"
        },
        "score": {
            "score_inputs": {
                field: 5
                for field in SCORE_FIELDS
            }
        }
    }

    result = calculate_score(record)

    passed = (
        result["total"] == 40
        and result["score_status"] == "COMPLETE"
        and result["missing_inputs"] == []
    )

    print(
        f"Calculated total: {result['total']}"
    )

    print("Result: PASS" if passed else "Result: FAIL")

    return passed


def test_missing_score():
    print()
    print("Test 3: Missing Score Input")
    print("=" * 50)

    record = {
        "candidate_id": "TEST-002",
        "compound": {
            "name": "Test Compound"
        },
        "score": {
            "score_inputs": {
                "target_relevance": 5,
                "mechanism_evidence": None,
                "potency_evidence": 3,
                "selectivity_evidence": 3,
                "adme_evidence": 4,
                "safety_evidence": 4,
                "research_development_evidence": 5,
                "evidence_completeness": 4
            }
        }
    }

    result = calculate_score(record)

    passed = (
        result["total"] is None
        and result["score_status"] == "INCOMPLETE"
        and "mechanism_evidence" in result["missing_inputs"]
    )

    print("Result: PASS" if passed else "Result: FAIL")

    return passed


def test_deterministic_scoring(records):
    print()
    print("Test 4: Deterministic Scoring")
    print("=" * 50)

    first = create_comparison_results(records)
    second = create_comparison_results(records)

    passed = first == second

    print("Result: PASS" if passed else "Result: FAIL")

    return passed


def test_tie_handling():
    print()
    print("Test 5: Deterministic Tie Handling")
    print("=" * 50)

    records = [
        {
            "candidate_id": "C-002",
            "compound": {
                "name": "Compound B"
            },
            "score": {
                "score_inputs": {
                    field: 4
                    for field in SCORE_FIELDS
                }
            }
        },
        {
            "candidate_id": "C-001",
            "compound": {
                "name": "Compound A"
            },
            "score": {
                "score_inputs": {
                    field: 4
                    for field in SCORE_FIELDS
                }
            }
        }
    ]

    results = create_comparison_results(records)

    passed = (
        results[0]["candidate_id"] == "C-001"
        and results[1]["candidate_id"] == "C-002"
    )

    print("Result: PASS" if passed else "Result: FAIL")

    return passed


def print_results(results):
    print()
    print("Comparison Results")
    print("=" * 70)

    for result in results:
        score = result["score"]

        if score["total"] is None:
            print(
                f"{result['candidate_id']} | "
                f"{result['compound_name']} | "
                f"INCOMPLETE | "
                f"Missing: {', '.join(score['missing_inputs'])}"
            )
        else:
            print(
                f"Rank {result['rank']} | "
                f"{result['candidate_id']} | "
                f"{result['compound_name']} | "
                f"{score['total']}/{score['maximum']}"
            )


def main():
    print("TB Drug Discovery Comparison and Scoring")

    records = load_records()

    print(f"Loaded records: {len(records)}")

    if not records:
        print("No records available.")
        return

    results = create_comparison_results(records)

    save_results(results)

    print_results(results)

    test_score_normalization()
    test_complete_score()
    test_missing_score()
    test_deterministic_scoring(records)
    test_tie_handling()

    print()
    print("Phase 6 scoring engine completed.")


if __name__ == "__main__":
    main()