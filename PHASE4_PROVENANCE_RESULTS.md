# Phase 4 — Candidate Evidence Provenance Results

## 1. Objective

The objective of Phase 4 was to introduce provenance information into canonical candidate records.

Provenance helps distinguish original source information from fields generated through normalization or other processing.

## 2. Implementation

The implementation is maintained in:

- `candidate_provenance.py`
- `candidate_records_with_provenance.json`

The provenance layer records:

- Original record source
- Schema version
- Transformation description
- Derived fields

## 3. Provenance Structure

Each processed candidate record includes a provenance section containing:

| Field | Description |
|---|---|
| `record_source` | Original input source |
| `schema_version` | Canonical schema version |
| `transformation` | Description of the record transformation |
| `derived_fields` | Fields generated or derived during processing |

## 4. Source and Derived Information

The implementation distinguishes:

- Original candidate source information
- Derived comparison information
- Score information
- Interpretation information

Derived information should not be represented as original scientific evidence.

## 5. Previously Reported Verification

The previous local execution reported that all seven provenance tests passed.

This result is historical and should be reproduced using the current repository files before independent verification.

## 6. Output

Generated output:

`candidate_records_with_provenance.json`

Input:

`candidate_records_v1.json`

Original registry:

`candidate_compounds.csv`

## 7. Limitations

The provenance layer records processing information. It does not independently validate the scientific accuracy of source publications or experimental findings.

Source citations and individual evidence claims require separate verification.

## 8. Status

**Implementation status:** Previously implemented locally.

**Documentation status:** Restored.

**Independent GitHub verification:** Pending.
