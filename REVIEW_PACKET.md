\# REVIEW PACKET



\## 1. Project Overview



\*\*Project:\*\* Shamit — New Drug Discovery Research \& Candidate Compound Intelligence Foundation



\*\*Programme:\*\* Biotech Learnship – Test 1



\*\*Research Area:\*\* Tuberculosis (TB)



This project demonstrates a structured beginner-level workflow for drug discovery research, candidate compound documentation, evidence comparison, evidence-gap analysis, Python-based data handling, and testing.



The project is intended for educational research and evidence organization.



\---



\## 2. Entry Point



The main research dataset is:



`phase3\\candidate\_compounds.csv`



The main Python research pipeline is:



`phase3\\drug\_discovery\_pipeline.py`



The CSV contains 10 TB candidate compounds and 17 data fields for each candidate.



\---



\## 3. Core Execution Flow



The project follows this workflow:



1\. Learn drug discovery fundamentals

2\. Identify research data sources

3\. Define the TB research area

4\. Select candidate compounds

5\. Collect candidate evidence

6\. Store candidate data in CSV format

7\. Compare candidates using an evidence-strength framework

8\. Identify evidence gaps

9\. Build a Python research pipeline

10\. Test the pipeline and dataset

11\. Document results

12\. Prepare the final review and handover packet



\---



\## 4. Candidate Dataset



The project currently contains 10 candidates:



| ID    | Candidate    |

| ----- | ------------ |

| C-001 | Rifampicin   |

| C-002 | Isoniazid    |

| C-003 | Pyrazinamide |

| C-004 | Ethambutol   |

| C-005 | Bedaquiline  |

| C-006 | Delamanid    |

| C-007 | Pretomanid   |

| C-008 | Linezolid    |

| C-009 | Clofazimine  |

| C-010 | Sutezolid    |



The candidate dataset contains:



\* Candidate ID

\* Compound name

\* Synonyms

\* Source database

\* Molecular identifier

\* Target

\* Mechanism of action

\* Therapeutic area

\* Evidence stage

\* Potency

\* Selectivity

\* ADME

\* Safety/toxicity

\* Supporting publications

\* Known limitations

\* Evidence confidence

\* Missing information



\---



\## 5. Python Pipeline



The Python pipeline provides:



\* CSV loading

\* Compound search

\* Synonym search

\* Therapeutic-area filtering

\* Evidence-stage filtering

\* Candidate listing

\* Individual candidate details

\* All candidate details

\* Invalid candidate handling

\* Invalid menu-choice handling



Python version used:



\*\*Python 3.14.3\*\*



The Python launcher used:



`py`



\---



\## 6. Sample Execution



The pipeline was tested using the TB candidate dataset.



Expected dataset:



\*\*10 candidates\*\*



The pipeline successfully loaded and processed the candidate records.



Example operations tested:



\* Search for a valid compound

\* Search for an unknown compound

\* Filter by therapeutic area

\* Filter by evidence stage

\* View candidate details

\* View all candidates

\* Exit the program



\---



\## 7. Candidate Comparison



The candidates were compared using 8 evidence-strength criteria:



1\. Target relevance

2\. Mechanism evidence

3\. Potency evidence

4\. Selectivity evidence

5\. ADME evidence

6\. Safety evidence

7\. Research/development evidence

8\. Evidence completeness



Each criterion uses a 0–5 scale.



Maximum score:



\*\*40 points\*\*



The scoring represents the strength and completeness of documented evidence. It does not represent clinical superiority or a treatment recommendation.



The comparison results are stored in:



`phase3\\phase4\\candidate\_comparison\_results.csv`



\---



\## 8. Evidence Gap Analysis



Phase 6 identified incomplete or missing evidence in the candidate dataset.



Common evidence gaps include:



\* Quantitative potency

\* Quantitative selectivity

\* Detailed assay-specific evidence

\* Human pharmacokinetic information

\* Detailed safety information

\* Complete ADME information



The evidence-gap files are stored in:



`phase3\\phase6\\`



Important files include:



\* `EVIDENCE\_GAP\_TABLE.md`

\* `EVIDENCE\_GAP\_PRIORITY.md`

\* `EVIDENCE\_GAP\_REPORT.md`

\* `PHASE6\_EVIDENCE\_GAP\_ANALYSIS.md`

\* `PHASE6\_COMPLETE.md`



Where reliable structured evidence was not available, information was recorded as:



`UNKNOWN / NOT FOUND`



\---



\## 9. Testing Evidence



Phase 7 testing has been completed.



\### Overall Result



\*\*16/16 functional tests passed\*\*



Testing covered:



\* Valid candidate search

\* Unknown candidate handling

\* Duplicate candidate ID detection

\* Missing compound name detection

\* Incomplete record detection

\* Invalid evidence-stage detection

\* Missing evidence-field detection

\* Comparison with incomplete data

\* CSV schema validation

\* Dataset completeness



\### CSV Schema Test



Expected columns:



\*\*17\*\*



Actual columns:



\*\*17\*\*



Result:



\*\*PASS\*\*



\### Dataset Completeness



All 10 candidates were checked for data completeness.



Result:



\*\*PASS\*\*



Detailed testing documentation:



`phase3\\phase7\\PHASE7\_TEST\_PLAN.md`



`phase3\\phase7\\PHASE7\_TEST\_RESULTS.md`



\---



\## 10. Failure Cases Tested



The project included deliberate test cases for:



\* Duplicate candidate IDs

\* Missing compound names

\* Incomplete candidate records

\* Invalid evidence stages

\* Missing potency information

\* Missing selectivity information

\* Incomplete comparison data

\* Invalid test CSV data



These tests were used to verify that data-quality problems could be identified rather than silently ignored.



\---



\## 11. What Changed During the Project



The initial research direction focused on \*\*EGFR-mutated non-small-cell lung cancer (NSCLC)\*\*.



The research direction was later changed to:



\*\*Tuberculosis (TB)\*\*



The candidate dataset and research workflow were updated to reflect the TB research area.



The final pipeline therefore uses the 10 TB candidates listed in Section 4.



\---



\## 12. Known Limitations



The project has several limitations:



\* The dataset does not represent all TB drug research.

\* Some potency values are unavailable.

\* Some selectivity values are unavailable.

\* Some detailed ADME information is incomplete.

\* Some safety information requires further structured extraction.

\* Evidence quality varies between candidates.

\* Some information should be further verified against primary scientific sources.

\* Comparison scores represent evidence strength rather than clinical effectiveness.

\* The pipeline does not perform laboratory experiments.

\* The pipeline does not synthesize, manufacture, administer, or recommend drugs.



\---



\## 13. Current Project Status



\### Completed



\* Phase 1 — Drug Discovery Fundamentals

\* Phase 2 — Research Data Sources

\* Phase 3 — Candidate Compound Research

\* Phase 4 — Candidate Comparison

\* Phase 5 — Python Research Pipeline

\* Phase 6 — Evidence Gap Analysis

\* Phase 7 — Testing and Validation



\### Current Phase



\*\*Phase 8 — Documentation, Review and Handover\*\*



\---



\## 14. Recommended Next Work



The remaining work is focused on final documentation and review.



Recommended activities:



1\. Verify all required project files

2\. Review README documentation

3\. Review the review packet

4\. Confirm test evidence

5\. Confirm project structure

6\. Record final limitations

7\. Prepare the final handover summary

8\. Perform a final project review



\---



\## 15. Final Handover Statement



The project provides a structured educational foundation for TB drug discovery research and candidate compound intelligence.



It demonstrates:



\* Research-area definition

\* Candidate identification

\* Scientific evidence organization

\* Structured CSV data management

\* Evidence-based candidate comparison

\* Evidence-gap analysis

\* Python-based research data handling

\* Functional testing

\* Documentation and review preparation



The current project status is suitable for final documentation and handover review.



