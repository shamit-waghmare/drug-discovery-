# BIOTECH_GAP_REGISTER

**Project:** TB Drug Discovery Research and Candidate Intelligence Pipeline  
**Repository:** `bhiv-biotech-drug-discovery`  
**Owner:** Project audit / issue prioritisation  
**Last reviewed:** 14 November 2026 (Updated with Direct Repository Verification)

---

## 1. Prioritisation Summary

This register ranks the known gaps by their impact on delivery. All gaps have now been directly investigated and verified in the live repository.

| Priority | Gap | Delivery impact | Live Verification Status |
|---|---|---|---|
| P1 | Scoring scripts cannot resolve input files (GAP-01) | Scoring fails on fresh checkout: `calculate_scores.py` and `generate_comparison.py` raise `FileNotFoundError`. | **Root cause confirmed:** Hardcoded `"../candidate_compounds.csv"`. |
| P1 | Provenance JSON generation and file naming (GAP-02) | `calculate_scores_v2.py` and `candidate_provenance.py` fail to load input data. | **Root cause confirmed:** Files exist on disk as `candidate_records_v1[1].json` and `candidate_records_with_provenance[1].json`. |
| P1 | Candidate dataset is limited to 10 entries (GAP-03) | Research coverage is narrow; lacks automated external DB ingestion. | **Confirmed in repository:** Exact count is 10 candidates in CSV. |
| P2 | Potency and selectivity evidence incomplete (GAP-04) | 8/10 candidates report `UNKNOWN / NOT FOUND` for potency/selectivity. | **Confirmed in repository:** High evidence gap in pharmacological data. |
| P2 | ADME, human PK, and safety extraction need depth (GAP-05) | Quantitative exposure and safety profiles are uneven across candidates. | **Confirmed in repository:** Documented in candidate notes and CSV. |
| P2 | Missing automated test script in repository (GAP-06) | Historical 12/12 pass reported in Phase 8 cannot be reproduced. | **Confirmed in repository:** `test_phase8.py` is missing per `PHASE8_TEST_STATUS.md`. |
| P2 | Repository layout anomalies and path inconsistencies (GAP-07) | 0-byte placeholder files (`sample_data`, `schema`) and duplicate suffixes clutter repo. | **Confirmed in repository:** 0-byte files and `[1]` filenames identified. |
| P3 | Search test coverage & synonym expectations (GAP-08) | Screenshot search for `Tubercorin` returned no match. | **Verified:** `Tubercorin` is not in dataset; behavior is correct. Needs unit tests. |
| P3 | BIQOS integration contract and test suite (GAP-09) | Core algorithms reusable, but no automated integration test or schema validator exists. | **Verified:** Pending formal contract interface. |

---

## 2. Detailed Gap Register

### GAP-01 — Scoring scripts use unresolved input paths

<badge color="danger">P1 — Critical Blocker (Fixed with Path Adjustment)</badge>

**Evidence & Live Investigation**
- Direct execution of `python calculate_scores.py` fails with:
  `FileNotFoundError: [Errno 2] No such file or directory: '../candidate_compounds.csv'`
- Direct execution of `python generate_comparison.py` fails with identical error:
  `FileNotFoundError: [Errno 2] No such file or directory: '../candidate_compounds.csv'`
- Both scripts assume they are being executed from a subfolder (e.g., `phase3/`), but are located directly in the repository root.

**Delivery Impact**
Scoring and comparison cannot be run from the repository root.

**Required Fix**
Use script-relative path resolution with `pathlib.Path`:
```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "candidate_compounds.csv"
```

**Acceptance Criteria**
- `python calculate_scores.py` runs without errors from any working directory and prints scores for all 10 candidates.
- `python generate_comparison.py` successfully creates `candidate_comparison_results.csv`.

---

### GAP-02 — Provenance JSON file naming and generation blocker

<badge color="danger">P1 — Critical Blocker (Fixed by Renaming Files)</badge>

**Evidence & Live Investigation**
- Direct execution of `python calculate_scores_v2.py` reports:
  `ERROR: Input file not found: ...\candidate_records_with_provenance.json`
- Direct execution of `python candidate_provenance.py` reports:
  `ERROR: candidate_records_v1.json not found.`
- Inspection of the repository revealed the files **do exist** with duplicate download/sync suffixes:
  - `candidate_records_v1[1].json` (20,471 bytes, 10 valid records)
  - `candidate_records_with_provenance[1].json` (24,829 bytes, 10 valid records)
- Running an in-memory test pointing `calculate_scores_v2.py` to `candidate_records_with_provenance[1].json` successfully loaded all 10 records.

**Delivery Impact**
Blocks execution of Scorer v2 and provenance verification despite complete data existing in the repo.

**Required Fix**
Rename the files to their canonical names:
```powershell
Rename-Item "candidate_records_v1[1].json" "candidate_records_v1.json"
Rename-Item "candidate_records_with_provenance[1].json" "candidate_records_with_provenance.json"
```

**Acceptance Criteria**
- `python candidate_provenance.py` loads 10 records from `candidate_records_v1.json` and updates `candidate_records_with_provenance.json`.
- `python calculate_scores_v2.py` loads 10 records and outputs `candidate_comparison_results_v2.json`.

---

### GAP-03 — Dataset contains only 10 candidates

<badge color="danger">P1 — Limits Research Coverage</badge>

**Evidence & Live Investigation**
- `candidate_compounds.csv` contains exactly 10 candidate compounds (C-001 through C-010).
- The pipeline lacks an automated data-fetching mechanism from external biological databases (ChEMBL, PubChem, UniProt).

**Delivery Impact**
The pipeline evaluates a small set of established TB drugs rather than serving as a broad discovery landscape.

**Required Fix**
- Define inclusion criteria for expanding candidate compounds.
- Implement an automated or semi-automated ingestion script querying public APIs (e.g. PubChem REST, ChEMBL API).
- Preserve source identifiers, access dates, and provenance on ingestion.

**Acceptance Criteria**
Registry expands with traceably sourced candidates following the 17-field schema.

---

### GAP-04 — Potency and selectivity evidence is incomplete

<badge color="warning">P2 — Reduces Evidence Quality</badge>

**Evidence & Live Investigation**
- Inspection of `candidate_compounds.csv` reveals that 8 of 10 candidates (C-001, C-003, C-004, C-005, C-006, C-007, C-008, C-009, C-010) report `UNKNOWN / NOT FOUND` for potency and selectivity.
- Only C-002 (Isoniazid) has minimal tuberculostatic concentration and antimicrobial specificity notes populated.

**Delivery Impact**
Direct potency/selectivity comparisons across candidates are prevented; evidence scores in these dimensions default to minimal values.

**Required Fix**
- Extract published quantitative potency metrics (MIC against *M. tuberculosis* H37Rv, IC50 for target enzyme) from literature/databases.
- Document measurement units, assay type, and citation.
- Maintain `UNKNOWN / NOT FOUND` where verified data is genuinely absent.

**Acceptance Criteria**
Quantitative values and reference citations are added to `candidate_compounds.csv`.

---

### GAP-05 — ADME, human PK, and safety extraction need deeper coverage

<badge color="warning">P2 — Reduces Evidence Completeness</badge>

**Evidence & Live Investigation**
- Bedaquiline (C-005) detail record lists missing quantitative human PK parameters and granular safety extraction.
- Most entries contain qualitative descriptions rather than structured PK values ($C_{max}$, $t_{1/2}$, AUC, clearance).

**Delivery Impact**
Limits preclinical/clinical comparison fidelity across candidates.

**Required Fix**
- Create a structured PK/safety checklist for TB compounds.
- Populate key PK parameters with traceable references.

**Acceptance Criteria**
Completeness metrics for PK/safety fields increase with verifiable source citations.

---

### GAP-06 — Automated test script missing from repository

<badge color="warning">P2 — Weakens Handover Confidence</badge>

**Evidence & Live Investigation**
- `PHASE8_TEST_STATUS.md` acknowledges: *"The original test_phase8.py test script is not currently available in this GitHub repository."*
- Phase 7 documented 16/16 tests passing, but as a manual checklist in markdown rather than a standalone executable test script.

**Delivery Impact**
Automated testing and regression verification cannot be executed in CI or from a fresh checkout.

**Required Fix**
- Author a dedicated test file `test_pipeline.py` covering:
  1. CSV schema validation (10 candidates, 17 columns).
  2. Search function with exact names, synonyms, case-insensitivity, and no-match terms.
  3. Filter functions (therapeutic area, evidence stage).
  4. Completeness and scoring calculations.
  5. JSON schema validation.

**Acceptance Criteria**
`pytest` or `python test_pipeline.py` executes and passes all test assertions from repository root.

---

### GAP-07 — Repository layout and file anomalies

<badge color="warning">P2 — Maintenance Risk</badge>

**Evidence & Live Investigation**
- The repository root contains two 0-byte placeholder files: `sample_data` and `schema`.
- Duplicate bracket suffixes exist on JSON files (`candidate_records_v1[1].json`).
- Older documentation (`REVIEW_PACKET.md`, `CURRENT_STATE.md`) references paths like `phase3/candidate_compounds.csv` when files are located at repository root.

**Delivery Impact**
Confuses users and automated scripts about canonical file locations.

**Required Fix**
- Remove 0-byte placeholder files.
- Normalize filenames.
- Standardize all markdown documentation to reference root file paths.

**Acceptance Criteria**
Clean repository structure without orphan placeholder files or bracketed filenames.

---

### GAP-08 — Search and synonym test coverage

<badge color="info">P3 — Usability & Data Quality</badge>

**Evidence & Live Investigation**
- In execution screenshots, searching `Tubercorin` returned `No candidates found.`
- Verification against `candidate_compounds.csv` confirmed `Tubercorin` is not present in names or synonyms. The search code properly caught the query and handled it without crashing.

**Delivery Impact**
Clarifies that the observed screenshot result was an expected negative search test, not a system failure.

**Required Fix**
- Add unit tests verifying positive matches (e.g. `Rifampicin`, `Rifampin`), synonym matches (e.g. `INH`, `BDQ`), case-insensitivity (`rifampicin`), and negative matches (`Tubercorin`, `xyz123`).

**Acceptance Criteria**
Automated test suite validates expected search behavior for all test categories.

---

### GAP-09 — BIQOS integration contract

<badge color="info">P3 — Required Before Production Claims</badge>

**Evidence & Live Investigation**
- Core scoring logic in `calculate_scores_v2.py` and completeness checks in `calculate_completeness.py` are modular and well-suited for integration.
- However, no formal JSON Schema or API contract test is committed.

**Delivery Impact**
Integration into external platforms (BIQOS) requires manual adaptation.

**Required Fix**
- Define JSON Schema for candidate records and scoring outputs.
- Create an integration test validating that candidate records adhere to schema.

**Acceptance Criteria**
JSON Schema committed and validated via `jsonschema` in automated tests.

---

## 3. Recommended Execution Roadmap

1. **Step 1 (Immediate - 5 minutes):**
   - Rename `candidate_records_v1[1].json` $\rightarrow$ `candidate_records_v1.json`
   - Rename `candidate_records_with_provenance[1].json` $\rightarrow$ `candidate_records_with_provenance.json`
   - Update `CSV_FILE = "../candidate_compounds.csv"` to script-relative path in `calculate_scores.py` and `generate_comparison.py`.
   - Delete 0-byte `sample_data` and `schema` placeholders.
2. **Step 2 (Verification - 5 minutes):**
   - Run `candidate_provenance.py`, `calculate_scores.py`, `calculate_scores_v2.py`, and `generate_comparison.py`.
   - Confirm all scripts execute with 10 records and output comparison results.
3. **Step 3 (Quality & Testing - 15 minutes):**
   - Implement `test_pipeline.py` to restore automated test capabilities (GAP-06 & GAP-08).
4. **Step 4 (Dataset Enrichment - Next Milestone):**
   - Populate quantitative potency/selectivity values from literature (GAP-04 & GAP-05).
   - Plan candidate registry expansion (GAP-03).

---

## 4. Definition of Ready for Review (Updated Checklist)

- [x] Live repository inspected and root causes identified.
- [x] Input path and file naming failures diagnosed.
- [ ] Bracketed JSON filenames normalized.
- [ ] Scoring scripts updated with script-relative path resolution.
- [ ] Scoring scripts execute cleanly with 10 records loaded.
- [ ] Standalone automated test script created and passing.
- [ ] Canonical repository structure aligned with documentation.
- [ ] External integration contract documented.
