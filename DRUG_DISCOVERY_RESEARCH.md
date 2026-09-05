# Drug Discovery Research

## 1. Research Area

The project focuses on Tuberculosis (TB) and the structured research of candidate compounds relevant to TB drug discovery.

## 2. Research Objective

The objective is to build a beginner-level research pipeline that identifies candidate compounds, organizes scientific evidence, compares candidates using defined criteria, and records evidence gaps.

## 3. Drug Discovery Workflow

The project follows these major stages:

1. Target Identification
2. Target Validation
3. Hit Identification
4. Hit-to-Lead
5. Lead Optimization
6. Preclinical Evaluation
7. Clinical Development
8. Regulatory Evaluation

## 4. Candidate Compounds

The current candidate set contains 10 compounds:

- C-001 Rifampicin
- C-002 Isoniazid
- C-003 Pyrazinamide
- C-004 Ethambutol
- C-005 Bedaquiline
- C-006 Delamanid
- C-007 Pretomanid
- C-008 Linezolid
- C-009 Clofazimine
- C-010 Sutezolid

## 5. Evidence Collection

For each candidate, the project records:

- Molecular identifiers
- Target
- Mechanism of action
- Therapeutic area
- Evidence stage
- Potency
- Selectivity
- ADME
- Safety/toxicity
- Supporting publications
- Known limitations
- Evidence confidence
- Missing information

## 6. Candidate Comparison

Candidates are compared using an evidence-strength scoring framework. Scores are used to organize the available evidence and do not represent clinical superiority or treatment recommendations.

## 7. Evidence Gap Analysis

Important evidence gaps identified during the project include:

- Quantitative potency information
- Quantitative selectivity information
- Assay-specific evidence
- Human pharmacokinetic evidence
- Detailed safety information
- Complete ADME information

## 8. Python Research Pipeline

The project includes a Python-based pipeline for loading the candidate CSV, searching candidates, filtering candidates, calculating completeness, and supporting evidence-based comparison.

Main pipeline:

phase3\drug_discovery_pipeline.py

## 9. Data Structure

The candidate registry uses a 17-field CSV schema:

candidate_id, compound_name, synonyms, source_database, molecular_identifier, target, mechanism_of_action, therapeutic_area, evidence_stage, potency, selectivity, adme, safety_toxicity, supporting_publications, known_limitations, evidence_confidence, missing_information

## 10. Scope and Limitations

This is an educational research and evidence-management project. It is not a substitute for professional medical, regulatory, clinical, or laboratory evaluation.

The project does not include drug synthesis, laboratory experimentation, manufacturing instructions, dosing instructions, or treatment recommendations.

## 11. Current Status

Phases 1 through 7 have been completed.

Phase 8 — Documentation and Handover — has been completed.

## 12. Next Step

The final documentation and project verification have been completed. The project is ready for review and handover.

