\# CURRENT STATE — TB Drug-Discovery Candidate Intelligence



\## 1. Project



\*\*Project:\*\* BHIV Biotech — TB Drug-Discovery Candidate Intelligence



\*\*Task ID:\*\* BIOTECH-T3-SHAMIT-TB-DRUG-DISCOVERY



\*\*Phase:\*\* Phase 1 — Existing-State Audit



\*\*Audit Date:\*\* 29/09/2026



\*\*Status:\*\* WORKING



\---



\## 2. Existing Capability



The existing TB drug-discovery project contains a candidate-compound registry, source/evidence information, candidate search and filtering, candidate comparison and scoring, completeness analysis, evidence-gap analysis, and an executable Python pipeline.



Existing work is preserved.



No existing repositories, datasets, scripts, or documents are being deleted.



\---



\## 3. Candidate Registry



The current registry contains 10 TB candidate compounds:



1\. C-001 — Rifampicin

2\. C-002 — Isoniazid

3\. C-003 — Pyrazinamide

4\. C-004 — Ethambutol

5\. C-005 — Bedaquiline

6\. C-006 — Delamanid

7\. C-007 — Pretomanid

8\. C-008 — Linezolid

9\. C-009 — Clofazimine

10\. C-010 — Sutezolid



Runtime verification confirmed:



\*\*Loaded candidates: 10\*\*



Status: \*\*IMPLEMENTED\*\*



\---



\## 4. Existing Files



| File/Folder                    | Purpose                                 | Current Status         |

| ------------------------------ | --------------------------------------- | ---------------------- |

| candidate\_compounds.csv        | TB candidate registry                   | Implemented            |

| drug\_discovery\_pipeline.py     | Candidate search/filter/detail pipeline | Implemented            |

| calculate\_completeness.py      | Candidate completeness calculation      | Implemented            |

| CANDIDATE\_COMPOUND\_REGISTRY.md | Candidate registry documentation        | Implemented/Documented |

| phase4/                        | Candidate comparison and scoring        | Implemented            |

| phase6/                        | Evidence-gap analysis                   | Implemented/Documented |

| phase7/                        | Edge-case testing material              | Implemented/Documented |

| PHASE5\_TEST\_RESULTS.md         | Phase 5 functional testing record       | Documented             |

| PHASE5\_PIPELINE.md             | Phase 5 pipeline documentation          | Documented             |

| PHASE5\_COMPLETE.md             | Phase 5 completion record               | Documented             |



\---



\## 5. Runtime Functional Audit



\### Candidate Loading



Test:



Pipeline startup.



Observed:



`Loaded candidates: 10`



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### Compound Search



Test:



`Rifampicin`



Observed:



`C-001 - Rifampicin`



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### Synonym Search



Test:



`Rifampin`



Observed:



`C-001 - Rifampicin`



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### Therapeutic-Area Filtering



Test:



`Tuberculosis`



Observed:



All 10 candidates returned.



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### Development-Stage Filtering



Test:



`Approved`



Observed:



C-001 through C-009 returned.



C-010 Sutezolid was excluded because its documented evidence stage is Investigational — Phase II.



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### Candidate Detail View



Test:



C-001 / Rifampicin



Observed:



Candidate details displayed.



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\### All Candidate Details



Test:



View all candidate details.



Observed:



All 10 candidate records displayed.



Status:



\*\*PASS — IMPLEMENTED\*\*



\---



\## 6. Completeness Audit



The existing completeness script was executed against all 10 candidates.



Observed results:



| Candidate          | Completeness |

| ------------------ | -----------: |

| C-001 Rifampicin   |          80% |

| C-002 Isoniazid    |         100% |

| C-003 Pyrazinamide |          90% |

| C-004 Ethambutol   |          80% |

| C-005 Bedaquiline  |          80% |

| C-006 Delamanid    |          80% |

| C-007 Pretomanid   |          80% |

| C-008 Linezolid    |          80% |

| C-009 Clofazimine  |          80% |

| C-010 Sutezolid    |          80% |



Status:



\*\*IMPLEMENTED\*\*



Test 3 enhancement required:



The current completeness calculation must be extended to validate the canonical Test 3 schema, including evidence, provenance, comparison attributes, score inputs, and review fields.



\---



\## 7. Comparison and Scoring Audit



The existing scoring system calculates:



1\. Target relevance

2\. Mechanism evidence

3\. Potency evidence

4\. Selectivity evidence

5\. ADME evidence

6\. Safety evidence

7\. Research/development evidence

8\. Evidence completeness



Maximum score:



\*\*40\*\*



Observed scores:



| Candidate          | Score |

| ------------------ | ----: |

| C-001 Rifampicin   | 30/40 |

| C-002 Isoniazid    | 34/40 |

| C-003 Pyrazinamide | 28/40 |

| C-004 Ethambutol   | 29/40 |

| C-005 Bedaquiline  | 32/40 |

| C-006 Delamanid    | 29/40 |

| C-007 Pretomanid   | 29/40 |

| C-008 Linezolid    | 30/40 |

| C-009 Clofazimine  | 25/40 |

| C-010 Sutezolid    | 24/40 |



Repeated execution with unchanged input produced the same results.



Status:



\*\*IMPLEMENTED — DETERMINISM VERIFIED\*\*



Test 3 enhancement required:



The scoring logic must explicitly document inputs, normalization, missing-data treatment, weighting, tie handling, and limitations.



\---



\## 8. Evidence-Gap Analysis



Existing Phase 6 work identified gaps involving:



\* Quantitative potency

\* Quantitative selectivity

\* Assay-specific evidence

\* Human pharmacokinetic information

\* Detailed ADME information

\* Detailed safety/toxicity evidence



The existing documentation explicitly distinguishes an evidence gap from negative evidence.



Status:



\*\*PARTIALLY IMPLEMENTED\*\*



Reason:



The existing project contains evidence-gap reports and prioritization, but Test 3 requires deterministic executable gap detection and structured gap outputs.



\---



\## 9. Candidate Identity Resolution



Current implementation supports:



\* Candidate-name search

\* Documented synonym search

\* Case-insensitive matching



Verified example:



`Rifampin` → `C-001 Rifampicin`



Status:



\*\*PARTIALLY IMPLEMENTED\*\*



Missing Test 3 requirements:



\* Exact candidate-ID matching rules

\* Normalized identifier matching

\* Ambiguous-name handling

\* False-positive prevention

\* Explicit unmatched-candidate handling

\* `HUMAN\_REVIEW\_REQUIRED` output

\* Preservation of ambiguous original records



\---



\## 10. Evidence and Provenance



The existing candidate dataset contains source/evidence information.



However, a formal provenance layer has not yet been established that consistently records:



\* Source

\* Source identifier

\* Citation/reference

\* Original record

\* Derived field

\* Transformation/normalization

\* Evidence limitation



Status:



\*\*PARTIALLY IMPLEMENTED\*\*



Test 3 enhancement required.



\---



\## 11. Automated Testing



Existing Phase 5 and Phase 7 testing material exists.



Documented tests include:



\* CSV loading

\* Candidate search

\* Synonym search

\* Therapeutic-area filtering

\* Evidence-stage filtering

\* Invalid input

\* Empty search results

\* Candidate detail retrieval

\* Edge-case testing



Status:



\*\*PARTIALLY IMPLEMENTED\*\*



Reason:



The existing testing material predates the complete Test 3 requirements.



The final Test 3 suite must explicitly cover:



TEST-01 Valid candidate

TEST-02 Missing candidate ID

TEST-03 Missing source

TEST-04 Duplicate candidate ID

TEST-05 Synonym matching

TEST-06 Ambiguous candidate identity

TEST-07 Incomplete evidence

TEST-08 Missing score input

TEST-09 Invalid input

TEST-10 Empty dataset

TEST-11 Comparison reproducibility

TEST-12 Deterministic repeated execution



\---



\## 12. Classification Summary



\### IMPLEMENTED



\* TB candidate registry

\* Candidate CSV loading

\* Candidate-name search

\* Synonym search

\* Therapeutic-area filtering

\* Development-stage filtering

\* Candidate detail retrieval

\* All-candidate detail retrieval

\* Existing completeness calculation

\* Existing comparison/scoring

\* Deterministic scoring verification

\* Existing evidence-gap analysis

\* Existing functional and edge-case testing material



\### PARTIALLY IMPLEMENTED



\* Canonical evidence structure

\* Evidence-gap engine

\* Candidate identity resolution

\* Evidence provenance

\* Completeness validation against Test 3 requirements

\* Automated Test 3 coverage

\* Scoring specification/documentation



\### DOCUMENTED ONLY / REQUIRES TEST 3 IMPLEMENTATION



\* Formal versioned candidate schema

\* Formal provenance schema

\* Ambiguous identity review handling

\* Structured Test 3 intelligence output

\* Integration contract

\* Evidence Packet

\* Code Packet

\* Review Packet

\* Live integration readiness



\### MISSING



\* Versioned canonical candidate schema

\* Deterministic identity-resolution module

\* Formal provenance layer

\* Test 3 validation engine

\* Formal integration contract

\* Final Test 3 automated test suite

\* Evidence packet structure

\* Review packet

\* Integration-ready structured interface



\### TO TEST



\* Ambiguous identity handling

\* Duplicate candidate IDs

\* Missing required fields

\* Missing score inputs

\* Empty dataset

\* Invalid records

\* Full deterministic pipeline execution

\* Structured output generation

\* Integration interface



\### NON-GOALS



This capability does not:



\* Establish clinical efficacy

\* Establish human safety

\* Approve a drug candidate

\* Make regulatory decisions

\* Replace scientific review

\* Treat an evidence score as scientific truth

\* Treat an evidence gap as negative evidence



\---



\## 13. Phase 1 Conclusion



The existing TB drug-discovery project provides a functioning foundation for the Final Test 3 candidate-intelligence capability.



The existing work is reusable and will be preserved.



The main Test 3 work is not to recreate the research dataset, but to convert the existing components into a deterministic, provenance-aware, schema-driven and integration-ready capability.



Next phase:



\*\*Phase 2 — Canonical Candidate Schema\*\*



