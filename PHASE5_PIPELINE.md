# Phase 5 — Mini Python Research Pipeline

## 1. Objective

The objective of Phase 5 was to build a beginner-level Python pipeline that can read the TB candidate compound dataset and allow basic research-oriented searching, filtering, and candidate-detail inspection.

## 2. Input Dataset

Input file:

`candidate_compounds.csv`

Number of candidates:

`10`

Research area:

`Tuberculosis (TB)`

## 3. Pipeline Functions

The pipeline provides the following functions:

- Load candidates from CSV
- Search by compound name
- Search by synonym
- Filter by therapeutic area
- Filter by evidence stage
- Display all candidates
- View details of one candidate
- View details of all candidates
- Handle invalid candidate IDs
- Handle empty search results
- Handle invalid menu choices
- Exit cleanly

## 4. Menu

The current pipeline menu is:

1. Search by compound name
2. Filter by therapeutic area
3. Filter by evidence stage
4. Show all candidates
5. View candidate details
6. View all candidate details
7. Exit

## 5. Candidate Detail Fields

The candidate-detail function displays:

- Candidate ID
- Compound name
- Synonyms
- Source database
- Molecular identifier
- Target
- Mechanism of action
- Therapeutic area
- Evidence stage
- Potency
- Selectivity
- ADME
- Safety/Toxicity
- Supporting publications
- Known limitations
- Evidence confidence
- Missing information

## 6. Testing Status

Phase 5 functional testing was completed successfully.

Tests included:

- CSV loading
- Compound search
- Synonym search
- Therapeutic-area filtering
- Evidence-stage filtering
- Case-insensitive searches
- Show-all function
- Candidate detail lookup
- Invalid candidate ID
- No-result searches
- Invalid menu choice
- Clean program exit

All planned tests passed.

## 7. Known Limitation

The pipeline currently performs local searches and filtering on the existing CSV dataset.

It does not automatically retrieve new scientific information from external databases or publications.

## 8. Conclusion

Phase 5 successfully produced a working beginner-level research pipeline for the TB candidate compound dataset.

The pipeline provides a reproducible way to inspect and search structured candidate evidence.

Phase 5 status:

**COMPLETE**# Phase 5 — Completion Record

## Status

**COMPLETE**

## Completed Work

- Built the Python research pipeline.
- Connected the pipeline to `candidate_compounds.csv`.
- Loaded 10 TB candidate compounds.
- Implemented compound-name and synonym search.
- Implemented therapeutic-area filtering.
- Implemented evidence-stage filtering.
- Implemented candidate-detail lookup.
- Implemented display of all candidate details.
- Added invalid-input handling.
- Tested case-insensitive searches.
- Tested no-result searches.
- Tested clean program exit.
- Documented all functional tests.

## Validation

All planned Phase 5 functional tests passed successfully.

## Main Files

- `drug_discovery_pipeline.py`
- `candidate_compounds.csv`
- `PHASE5_TEST_RESULTS.md`
- `PHASE5_PIPELINE.md`

## Known Limitation

The pipeline currently works with the existing local CSV dataset. It does not automatically retrieve new information from external scientific databases.

## Final Result

Phase 5 successfully produced a working beginner-level Python research pipeline for structured TB candidate-compound evidence.

**Phase 5 is complete.**