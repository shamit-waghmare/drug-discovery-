# Phase 7 — Test Results

## 1. Objective

Phase 7 verifies that the Tuberculosis (TB) drug discovery research pipeline functions correctly and handles expected and invalid inputs.

## 2. System Tested

The following project components were tested:

* `candidate_compounds.csv`
* `drug_discovery_pipeline.py`
* `calculate_completeness.py`

## 3. Dataset Validation

Expected candidates: **10**

Candidate IDs:

* C-001 Rifampicin
* C-002 Isoniazid
* C-003 Pyrazinamide
* C-004 Ethambutol
* C-005 Bedaquiline
* C-006 Delamanid
* C-007 Pretomanid
* C-008 Linezolid
* C-009 Clofazimine
* C-010 Sutezolid

Result:

**PASS**

The pipeline successfully loaded all 10 candidates.

## 4. Functional Test Results

| Test No. | Test                       | Expected Result              | Actual Result          | Status |
| -------- | -------------------------- | ---------------------------- | ---------------------- | ------ |
| 1        | CSV loading                | 10 candidates loaded         | 10 candidates loaded   | PASS   |
| 2        | Search Rifampicin          | C-001 returned               | C-001 returned         | PASS   |
| 3        | Search synonym Rifampin    | C-001 returned               | C-001 returned         | PASS   |
| 4        | TB therapeutic-area filter | 10 candidates                | 10 candidates          | PASS   |
| 5        | Approved-stage filter      | C-001 to C-009               | C-001 to C-009         | PASS   |
| 6        | Candidate details C-001    | Rifampicin details displayed | Details displayed      | PASS   |
| 7        | Invalid candidate C-999    | Error message                | Candidate ID not found | PASS   |
| 8        | Invalid menu input 9       | Error message                | Invalid choice message | PASS   |
| 9        | Empty search xyz123        | No candidates                | No candidates found    | PASS   |
| 10       | Lowercase compound search  | C-001 returned               | C-001 returned         | PASS   |
| 11       | Lowercase TB filter        | 10 candidates                | 10 candidates          | PASS   |
| 12       | Lowercase approved filter  | C-001 to C-009               | C-001 to C-009         | PASS   |
| 13       | Show all candidates        | 10 candidates                | 10 candidates          | PASS   |
| 14       | Show all candidate details | All 10 details displayed     | All 10 displayed       | PASS   |
| 15       | Unknown therapeutic area   | No candidates                | No candidates found    | PASS   |
| 16       | Clean exit                 | Program exits normally       | Exiting pipeline       | PASS   |

## 5. Test Summary

Total tests performed:

**16**

Passed:

**16**

Failed:

**0**

Overall result:

**16/16 PASS**

## 6. Error Handling

The pipeline correctly handled:

* Invalid menu selections
* Unknown candidate IDs
* Searches with no matching candidates
* Unknown therapeutic areas
* Case-insensitive search terms
* Case-insensitive filter values
* Clean program termination

## 7. Dataset Consistency

The pipeline successfully processed the complete 10-candidate TB dataset without runtime errors during the functional tests.

The candidate IDs were correctly maintained from C-001 through C-010.

## 8. Important Limitation

These tests verify software behavior and dataset handling.

They do not validate:

* Clinical effectiveness
* Clinical safety
* Treatment recommendations
* Drug superiority
* Experimental drug performance

Scientific evidence quality remains dependent on the underlying research sources and the completeness of the dataset.

## 9. Conclusion

Phase 7 functional testing was successfully completed.

All 16 planned tests passed.

The Python research pipeline successfully loads the TB candidate dataset, searches candidates, filters records, displays candidate information, handles invalid inputs, and exits cleanly.

**Phase 7 functional testing: INITIAL FUNCTIONAL TESTS COMPLETE**
## 10. Completeness Check

The `calculate_completeness.py` script was executed against the 10-candidate TB dataset.

| Candidate          | Completeness | Status |
| ------------------ | -----------: | ------ |
| C-001 Rifampicin   |          80% | PASS   |
| C-002 Isoniazid    |         100% | PASS   |
| C-003 Pyrazinamide |          90% | PASS   |
| C-004 Ethambutol   |          80% | PASS   |
| C-005 Bedaquiline  |          80% | PASS   |
| C-006 Delamanid    |          80% | PASS   |
| C-007 Pretomanid   |          80% | PASS   |
| C-008 Linezolid    |          80% | PASS   |
| C-009 Clofazimine  |          80% | PASS   |
| C-010 Sutezolid    |          80% | PASS   |

The completeness checker successfully processed all 10 candidates and identified differences in evidence completeness without producing runtime errors.

This confirms that the dataset contains incomplete evidence fields that can be detected programmatically.

**Completeness check: PASS**
## 11. Edge-Case Test Results

The invalid test dataset was tested separately from the main TB candidate dataset.

| Test                   | Expected Result                             | Actual Result            | Status |
| ---------------------- | ------------------------------------------- | ------------------------ | ------ |
| Duplicate candidate ID | Duplicate should be detected                | C-011 detected           | PASS   |
| Missing compound name  | Missing name should be detected             | C-012 detected           | PASS   |
| Incomplete record      | Incomplete record should be detected        | C-012 and C-013 detected | PASS   |
| Invalid evidence stage | Invalid or missing stage should be detected | C-013 and C-014 detected | PASS   |

### Edge-Case Test Summary

Rows tested: **5**

All intentionally introduced data-quality problems were detected.

**Edge-case testing: PASS**

### Note

C-013 has a blank evidence-stage field, so it is correctly reported as an invalid/missing evidence stage as well as an incomplete record.
## 12. Missing Evidence Field Test

The candidate dataset was checked for evidence fields that were blank or explicitly marked as unknown/not found.

| Candidate         | Missing/Unknown Evidence | Status |
| ----------------- | ------------------------ | ------ |
| C-009 Clofazimine | Potency, Selectivity     | PASS   |
| C-010 Sutezolid   | Potency, Selectivity     | PASS   |

The test successfully identified candidates where quantitative potency and selectivity evidence is currently unavailable or recorded as unknown.

**Missing-evidence testing: PASS**

### Interpretation

These results represent evidence gaps in the research dataset. They do not indicate that the compounds lack biological activity; they indicate that the required evidence was not sufficiently captured in the current dataset.
## 13. Comparison With Incomplete Data Test

The comparison dataset was checked to determine whether candidate records contain incomplete or unknown evidence before interpreting comparison scores.

**Expected result:** Candidates with missing or unknown evidence should be identified and should not be interpreted as having complete scientific evidence.

**Actual result:** 9 of the 10 candidates were identified as having at least one incomplete or unknown evidence field.

| Test                            | Expected Result                        | Actual Result         | Status |
| ------------------------------- | -------------------------------------- | --------------------- | ------ |
| Comparison with incomplete data | Incomplete evidence should be detected | 9 candidates detected | PASS   |

### Candidates Identified

* C-001 Rifampicin
* C-003 Pyrazinamide
* C-004 Ethambutol
* C-005 Bedaquiline
* C-006 Delamanid
* C-007 Pretomanid
* C-008 Linezolid
* C-009 Clofazimine
* C-010 Sutezolid

### Interpretation

The comparison results must be interpreted together with the evidence-completeness information. A numerical comparison score does not mean that all scientific evidence for a candidate is complete.

**Comparison-with-incomplete-data test: PASS**
## 14. CSV Schema Validation Test

The test dataset was checked against the required 17-column candidate-compound schema.

| Test                 | Expected Result     | Actual Result    | Status |
| -------------------- | ------------------- | ---------------- | ------ |
| CSV column structure | 17 required columns | 17 columns found | PASS   |
| Missing columns      | None                | None             | PASS   |
| Extra columns        | None                | None             | PASS   |

The test dataset has a valid CSV structure. It contains intentionally introduced data-quality problems such as duplicate candidate IDs, missing compound names, incomplete records, and invalid/missing evidence-stage values.

Therefore, the test confirms that the CSV structure is valid while the data-quality checks identify the intentionally introduced problems.

**CSV schema validation: PASS**
