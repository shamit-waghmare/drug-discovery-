TB Drug Discovery Research and Candidate Intelligence Pipeline

1. Project Overview

This project develops a structured research pipeline for organizing and evaluating tuberculosis (TB) drug-discovery candidate information.

It focuses on candidate compound records, evidence provenance, evidence completeness, evidence-gap identification, comparison, scoring, and retrieval.

Current status: Working local research pipeline. Production integration has not yet been demonstrated.

2. Project Objectives

* Maintain a structured TB candidate compound registry.
* Organize candidate information and source evidence.
* Support candidate identity matching.
* Track evidence provenance.
* Identify missing or incomplete evidence.
* Compare candidates using documented criteria.
* Support reproducible searches and analysis.

3. Current Repository Structure

The current GitHub repository contains files primarily in its root directory.

Important files include:

File	Purpose
drug_discovery_pipeline.py	Candidate retrieval and pipeline interface
candidate_compounds.csv	Candidate compound registry
candidate_provenance.py	Provenance processing
calculate_scores_v2.py	Updated candidate scoring
calculate_completeness.py	Evidence completeness calculation
CANDIDATE_COMPOUND_REGISTRY.md	Registry documentation
CANDIDATE_COMPARISON.md	Candidate comparison documentation
EVIDENCE_GAP_REPORT.md	Evidence-gap documentation
DATA_SOURCE_REGISTRY.md	Data-source documentation
CURRENT_STATE.md	Existing implementation status
REVIEW_PACKET.md	Project review documentation

Additional phase-wise documentation and implementation files are also maintained in the repository.

4. Pipeline Workflow

The intended research workflow is:

1. Candidate data collection
2. Canonical candidate record creation
3. Candidate identity matching
4. Evidence and provenance tracking
5. Evidence completeness assessment
6. Evidence-gap identification
7. Candidate comparison and scoring
8. Candidate search and retrieval
9. Automated validation

5. Candidate Scoring

The documented scoring framework contains eight dimensions:

1. Target relevance
2. Mechanism evidence
3. Potency evidence
4. Selectivity evidence
5. ADME evidence
6. Safety evidence
7. Research and development evidence
8. Evidence completeness

Each dimension has a documented scale of 0–5, giving a maximum possible score of 40.

Scores are intended for structured research comparison and decision support. They do not represent clinical efficacy, established safety, regulatory approval, or scientific truth.

Missing evidence must be treated as an evidence gap, not automatically as negative scientific evidence.

6. Testing Status

A local Phase 8 test execution previously reported:

* Total tests: 12
* Passed: 12
* Failed: 0

The test script and fresh execution evidence still need to be made available in the GitHub repository for independent reproduction.

7. BIQOS Integration Readiness

Potentially reusable components:

* Candidate record structure
* Candidate identity matching
* Provenance tracking
* Evidence completeness checks
* Evidence-gap reporting
* Candidate retrieval and filtering
* Deterministic comparison logic

Remaining work includes final repository organization, reproducible test evidence, integration contract verification, and independent integration testing.

No production BIQOS deployment is claimed.

8. Limitations

This project is a research-data organization and candidate-intelligence prototype.

It does not replace scientific review, laboratory validation, clinical evaluation, safety assessment, or regulatory decision-making.

9. Repository

GitHub: https://github.com/shamit-waghmare/drug-discovery-
