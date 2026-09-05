# Phase 5 — Mini Python Research Pipeline Test Results

## 1. Objective

The objective of Phase 5 was to build and test a beginner-level Python research pipeline for searching and filtering the TB candidate compound dataset.

## 2. Input Dataset

Input file:

`candidate_compounds.csv`

Total candidates loaded:

`10`

Disease area:

`Tuberculosis (TB)`

## 3. Pipeline Functions Tested

The following functions were tested:

- Load candidates from CSV
- Search by compound name
- Search by synonym
- Filter by therapeutic area
- Filter by evidence stage
- Display all candidates
- Handle invalid menu input
- Handle searches with no results
- Case-insensitive searching
- Clean program exit

## 4. Test Results

| Test | Expected Result | Status |
|---|---|---|
| CSV loading | 10 candidates loaded | PASS |
| Search Rifampicin | C-001 returned | PASS |
| Therapeutic area: Tuberculosis | 10 candidates returned | PASS |
| Evidence stage: Approved | 9 candidates returned | PASS |
| Invalid menu choice | Error message displayed | PASS |
| Show all candidates | 10 candidates displayed | PASS |
| Exit | Program exits without error | PASS |
| Search unknown compound | No candidates found | PASS |
| Filter unknown therapeutic area | No candidates found | PASS |
| Filter unknown evidence stage | No candidates found | PASS |
| Search synonym: Rifampin | C-001 returned | PASS |
| Lowercase compound search | C-001 returned | PASS |
| Lowercase therapeutic-area filter | 10 candidates returned | PASS |
| Lowercase evidence-stage filter | 9 candidates returned | PASS |

## 5. Evidence-Stage Test

The `Approved` filter correctly returned:

- C-001 Rifampicin
- C-002 Isoniazid
- C-003 Pyrazinamide
- C-004 Ethambutol
- C-005 Bedaquiline
- C-006 Delamanid
- C-007 Pretomanid
- C-008 Linezolid
- C-009 Clofazimine

C-010 Sutezolid was correctly excluded because its evidence stage is Investigational — Phase II.

## 6. Error Handling

The pipeline successfully handled:

- Invalid menu choices
- Searches with no matching candidates
- Therapeutic-area filters with no matching candidates
- Evidence-stage filters with no matching candidates

No program crash occurred during testing.

## 7. Conclusion

Phase 5 basic pipeline testing was completed successfully.

All planned functional tests passed.

The pipeline can currently:

1. Load the TB candidate dataset.
2. Search candidates by name or synonym.
3. Filter candidates by therapeutic area.
4. Filter candidates by evidence stage.
5. Display all candidates.
6. Handle invalid and empty-result searches.
7. Exit cleanly.

## 8. Known Limitation

The current pipeline displays candidate IDs and names only. It does not yet display the complete scientific evidence fields such as target, mechanism, potency, selectivity, ADME, safety, publications, and evidence gaps.

This can be addressed in the next improvement step.
## 9. Candidate Detail Tests

| Test | Expected Result | Status |
|---|---|---|
| View C-001 details | Complete Rifampicin record displayed | PASS |
| View C-999 | Candidate ID not found | PASS |
| View C-005 details | Complete Bedaquiline record displayed | PASS |
| View c-005 | C-005 details displayed successfully | PASS |

The candidate-detail function successfully retrieves and displays all 17 research fields from the CSV dataset. Candidate ID matching is case-insensitive.## 9. Candidate Details Tests

| Test | Expected Result | Status |
|---|---|---|
| View C-001 details | Full Rifampicin record displayed | PASS |
| Invalid candidate ID C-999 | "Candidate ID not found." displayed | PASS |
| View all candidate details | All 10 candidate records displayed | PASS |
| Clean exit after details tests | Program exits without error | PASS |

## 10. Final Phase 5 Status

Phase 5 basic functional testing is COMPLETE.

All planned tests passed successfully.

The pipeline can now search, filter, display candidate summaries, and display complete research records from the TB candidate dataset.