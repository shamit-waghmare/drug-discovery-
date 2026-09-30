import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "candidate_records_v1.json"
OUTPUT_FILE = BASE_DIR / "candidate_records_with_provenance.json"


SCHEMA_VERSION = "1.0.0"


def load_records():

    if not INPUT_FILE.exists():

        print("ERROR: candidate_records_v1.json not found.")

        return []

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def validate_provenance(record):

    provenance = record.get("provenance")

    if not isinstance(provenance, dict):

        return False

    required_fields = [
        "record_source",
        "schema_version",
        "transformation",
        "derived_fields"
    ]

    for field in required_fields:

        if field not in provenance:

            return False

    if not provenance["record_source"]:
        return False

    if not provenance["schema_version"]:
        return False

    if not provenance["transformation"]:
        return False

    if not isinstance(
        provenance["derived_fields"],
        list
    ):

        return False

    return True


def validate_source_evidence(record):

    source_evidence = record.get(
        "source_evidence"
    )

    if not isinstance(source_evidence, dict):

        return False

    sources = source_evidence.get("sources")

    if not isinstance(sources, list):

        return False

    if len(sources) == 0:

        return False

    evidence_summary = source_evidence.get(
        "evidence_summary"
    )

    if not isinstance(
        evidence_summary,
        dict
    ):

        return False

    limitations = source_evidence.get(
        "limitations"
    )

    if limitations is None:

        return False

    return True


def add_provenance(record):

    record = dict(record)

    record["provenance"] = {
        "record_source": "candidate_compounds.csv",
        "schema_version": SCHEMA_VERSION,
        "transformation": (
            "Mapped the original 17-field candidate "
            "registry into the version 1 canonical "
            "candidate structure while preserving "
            "source evidence separately from derived "
            "comparison and score fields."
        ),
        "derived_fields": [
            "derived_comparison",
            "score",
            "interpretation"
        ]
    }

    return record


def build_provenance_records(records):

    output = []

    for record in records:

        updated_record = add_provenance(record)

        output.append(updated_record)

    return output


def save_records(records):

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=2,
            ensure_ascii=False
        )


def test_source_evidence(records):

    print()
    print("Test 1: Source Evidence")
    print("=" * 60)

    passed = True

    for record in records:

        if not validate_source_evidence(record):

            passed = False

            print(
                "FAIL:",
                record.get("candidate_id")
            )

    if passed:

        print("All records contain source evidence.")
        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_provenance_fields(records):

    print()
    print("Test 2: Provenance Fields")
    print("=" * 60)

    passed = True

    for record in records:

        if not validate_provenance(record):

            passed = False

            print(
                "FAIL:",
                record.get("candidate_id")
            )

    if passed:

        print("All records contain required provenance fields.")
        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_schema_version(records):

    print()
    print("Test 3: Schema Version")
    print("=" * 60)

    passed = True

    for record in records:

        version = record.get(
            "provenance",
            {}
        ).get(
            "schema_version"
        )

        if version != SCHEMA_VERSION:

            passed = False

            print(
                "FAIL:",
                record.get("candidate_id"),
                version
            )

    if passed:

        print(
            "Schema version:",
            SCHEMA_VERSION
        )

        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_record_source(records):

    print()
    print("Test 4: Record Source")
    print("=" * 60)

    passed = True

    for record in records:

        source = record.get(
            "provenance",
            {}
        ).get(
            "record_source"
        )

        if source != "candidate_compounds.csv":

            passed = False

            print(
                "FAIL:",
                record.get("candidate_id")
            )

    if passed:

        print(
            "Record source:",
            "candidate_compounds.csv"
        )

        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_derived_fields(records):

    print()
    print("Test 5: Derived Fields")
    print("=" * 60)

    expected_fields = [
        "derived_comparison",
        "score",
        "interpretation"
    ]

    passed = True

    for record in records:

        derived_fields = record.get(
            "provenance",
            {}
        ).get(
            "derived_fields",
            []
        )

        for field in expected_fields:

            if field not in derived_fields:

                passed = False

                print(
                    "FAIL:",
                    record.get("candidate_id"),
                    field
                )

    if passed:

        print(
            "Derived fields:",
            ", ".join(expected_fields)
        )

        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_transformation(records):

    print()
    print("Test 6: Transformation Record")
    print("=" * 60)

    passed = True

    for record in records:

        transformation = record.get(
            "provenance",
            {}
        ).get(
            "transformation"
        )

        if not transformation:

            passed = False

            print(
                "FAIL:",
                record.get("candidate_id")
            )

    if passed:

        print("Transformation information is present.")
        print("Result: PASS")

    else:

        print("Result: FAIL")

    return passed


def test_deterministic_output(records):

    print()
    print("Test 7: Deterministic Provenance")
    print("=" * 60)

    first_output = build_provenance_records(
        records
    )

    second_output = build_provenance_records(
        records
    )

    if first_output == second_output:

        print(
            "Repeated provenance generation produced "
            "identical results."
        )

        print("Result: PASS")

        return True

    print("Result: FAIL")

    return False


def main():

    records = load_records()

    print(
        "Loaded canonical records:",
        len(records)
    )

    if not records:

        print("No records available.")

        return

    updated_records = build_provenance_records(
        records
    )

    save_records(updated_records)

    print(
        "Saved:",
        OUTPUT_FILE.name
    )

    test_source_evidence(updated_records)
    test_provenance_fields(updated_records)
    test_schema_version(updated_records)
    test_record_source(updated_records)
    test_derived_fields(updated_records)
    test_transformation(updated_records)
    test_deterministic_output(updated_records)

    print()
    print("Phase 4 provenance processing completed.")


if __name__ == "__main__":

    main()