# Shamit — New Drug Discovery Research & Candidate Compound Intelligence Foundation



## Project Overview



This project is a beginner-level drug discovery research and candidate compound intelligence pipeline focused on Tuberculosis (TB).



The project demonstrates how candidate compounds can be identified, documented, compared, tested, and evaluated for evidence completeness using structured research data and a simple Python pipeline.



## Research Area



**Therapeutic Area:** Tuberculosis (TB)



## Project Objective



The objective of this project is to build a structured research workflow for:



1\. Understanding the drug discovery process

2\. Identifying reliable research data sources

3\. Collecting information about candidate compounds

4\. Comparing candidate compounds using predefined evidence criteria

5\. Building a basic Python research pipeline

6\. Identifying missing or incomplete evidence

7\. Testing the research pipeline

8\. Preparing documentation and handover material



## Candidate Compounds



The current research dataset contains 10 TB-related candidate compounds:



| Candidate ID | Compound     |

| ------------ | ------------ |

| C-001        | Rifampicin   |

| C-002        | Isoniazid    |

| C-003        | Pyrazinamide |

| C-004        | Ethambutol   |

| C-005        | Bedaquiline  |

| C-006        | Delamanid    |

| C-007        | Pretomanid   |

| C-008        | Linezolid    |

| C-009        | Clofazimine  |

| C-010        | Sutezolid    |



## Project Structure



The main project work is organized under the `phase3` directory.



Important files include:



* `candidate_compounds.csv` — structured candidate compound dataset

* `CANDIDATE_COMPOUND_REGISTRY.md` — candidate research registry

* `drug_discovery_pipeline.py` — Python research pipeline

* `calculate_completeness.py` — evidence completeness checker

* `PHASE5_PIPELINE.md` — Phase 5 pipeline documentation

* `PHASE5_TEST_RESULTS.md` — Phase 5 test results

* `PHASE6_EVIDENCE_GAP_ANALYSIS.md` — evidence-gap analysis

* `EVIDENCE_GAP_TABLE.md` — evidence-gap table

* `EVIDENCE_GAP_PRIORITY.md` — evidence-gap priorities

* `EVIDENCE_GAP_REPORT.md` — evidence-gap report

* `PHASE6_COMPLETE.md` — Phase 6 completion record

* `phase4\\` — candidate comparison work

* `phase7\\` — testing documentation and test data



## Python Pipeline



The Python pipeline provides basic research-data operations:



* Search candidates by compound name

* Search candidates by synonym

* Filter by therapeutic area

* Filter by evidence stage

* Display all candidates

* Display individual candidate details

* Display all candidate details

* Handle invalid menu selections

* Handle unknown candidate IDs

* Handle searches with no matching results



## Candidate Comparison



Candidates were compared using an evidence-strength scoring framework.



The scoring criteria were:



1\. Target relevance

2\. Mechanism evidence

3\. Potency evidence

4\. Selectivity evidence

5\. ADME evidence

6\. Safety evidence

7\. Research/development evidence

8\. Evidence completeness



Each criterion uses a 0–5 evidence-strength scale.



The maximum possible score is **40**.



These scores represent the strength and completeness of the documented evidence. They do not represent clinical superiority, treatment recommendations, or guaranteed development success.



## Evidence Gap Analysis



The project identifies information that is missing, incomplete, or recorded as unknown.



Examples include:



* Quantitative potency information

* Quantitative selectivity information

* Detailed pharmacokinetic information

* Detailed safety evidence

* Assay-specific evidence



An evidence gap does not mean that a compound has no biological activity. It means that the required evidence was not sufficiently captured in the current research dataset.



## Testing



Phase 7 testing covered:



* CSV loading

* Candidate searching

* Synonym searching

* Therapeutic-area filtering

* Evidence-stage filtering

* Candidate-detail display

* Invalid candidate handling

* Invalid menu input

* Empty search results

* Case-insensitive searches and filters

* Dataset completeness

* Edge cases

* Missing evidence fields

* Comparison with incomplete data

* CSV schema validation



The functional test suite recorded **16/16 PASS**.



Additional completeness, edge-case, missing-evidence, incomplete-data, and CSV-schema tests also passed.



## Important Limitations



This project is a research and learning pipeline.



It does not:



* Manufacture drugs

* Synthesize compounds

* Perform laboratory experiments

* Provide treatment recommendations

* Determine clinical effectiveness

* Establish clinical safety

* Replace expert scientific review

* Establish that one candidate is clinically superior to another



Scientific conclusions depend on the quality, reliability, recency, and completeness of the underlying evidence sources.



## Current Status



| Phase                              | Status      |

| ---------------------------------- | ----------- |

| Phase 1 — Fundamentals             | COMPLETE    |

| Phase 2 — Data Sources             | COMPLETE    |

| Phase 3 — Candidate Research       | COMPLETE    |

| Phase 4 — Candidate Comparison     | COMPLETE    |

| Phase 5 — Python Pipeline          | COMPLETE    |

| Phase 6 — Evidence Gap Analysis    | COMPLETE    |

| Phase 7 — Testing                  | COMPLETE    |

| Phase 8 — Documentation & Handover | COMPLETE |



## Next Work



Phase 8 documentation, verification, pipeline smoke testing, and review/handover preparation have been completed.



## Project Metadata



**Owner:** TMS

**Research Area:** Tuberculosis (TB)

**Project Type:** Drug discovery research and candidate compound intelligence

**Convergence Status:** WORKING

**Semantic Confidence:** High

**Source Scope:** BHIV Master Directive vNEXT + SIPS Learnship Programme







