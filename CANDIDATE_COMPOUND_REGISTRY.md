# Phase 3 — Candidate Compound Research

## 1. Research Area

### Selected Disease

Tuberculosis (TB)

### Research Focus

Evidence-based research on antitubercular compounds and drug-development candidates relevant to tuberculosis treatment.

The research will include selected established and investigational compounds for which sufficient public evidence can be identified.

### Research Question

"What publicly available evidence exists for selected antitubercular compounds regarding their molecular identity, biological target, mechanism of action, potency, selectivity, ADME, safety/toxicity, development stage, supporting publications, limitations, and evidence gaps?"

### Research Objective

The objective is to build a structured, traceable research dataset that demonstrates how publicly available scientific and regulatory evidence can be collected and organized for TB-related compounds.

The objective is not to identify or declare a clinically superior drug.

### Scope

The research will examine, where available:

* Compound identity
* Synonyms
* Molecular identifiers
* Biological target
* Mechanism of action
* Therapeutic relevance to TB
* Development/evidence stage
* Potency information
* Selectivity information
* ADME information
* Safety/toxicity information
* Supporting publications
* Known limitations
* Evidence confidence
* Missing information
* Evidence gaps

### Evidence Sources

Evidence will be collected from appropriate public sources identified during Phase 2, including:

* PubChem
* ChEMBL
* PubMed
* Europe PMC
* ClinicalTrials.gov
* FDA
* Protein Data Bank
* WHO resources where relevant

Different sources will be used for different evidence types.

### Exclusions

This project does not include:

* Compound synthesis
* Laboratory experimentation
* Experimental testing
* Drug administration
* Clinical treatment recommendations
* Manufacturing procedures
* Claims that a compound is clinically superior
* Claims that a new medicine has been discovered

### Scientific Principle

The presence of a compound in a database, publication, or clinical-trial registry does not by itself establish that the compound is effective, safe, or clinically superior.

Evidence will be evaluated according to its source, relevance, experimental context, and completeness.

If reliable information cannot be established, the registry will record:

UNKNOWN / NOT FOUND

rather than making an unsupported assumption.

### Candidate Selection Status

Candidate selection: PENDING

Evidence extraction: PENDING

Candidate comparison: PENDING

Evidence-gap analysis: PENDING
## 2. Candidate Selection Criteria

The candidate list will be selected using predefined criteria rather than convenience or perceived drug quality.

A compound may be selected when it satisfies the following criteria:

### Criterion 1 — TB relevance

The compound must have documented relevance to tuberculosis treatment or TB drug development.

### Criterion 2 — Public evidence

Sufficient public information should be available to investigate the compound using one or more credible sources.

### Criterion 3 — Defined compound identity

The compound should have a sufficiently clear identity that it can be represented using a recognized name and, where available, a molecular identifier.

### Criterion 4 — Scientific evidence

There should be publicly documented scientific, clinical, regulatory, or other authoritative evidence relevant to the compound.

### Criterion 5 — Research diversity

The final set should provide a useful range of evidence stages, where possible, rather than containing only approved medicines.

### Criterion 6 — Evidence comparability

Each selected compound should have enough information to allow at least some common fields to be investigated across candidates.

### Criterion 7 — Traceability

Important candidate information must be traceable to identifiable public sources.

### Criterion 8 — No quality-based pre-ranking

Candidates will not be selected because they are assumed to be "best," "strongest," or "most promising."

The purpose of selection is to create a research dataset, not to establish a clinical ranking.

### Candidate Selection Decision

Each potential candidate will be evaluated against the criteria before being included.

Selection status will be recorded as:

INCLUDE

or

EXCLUDE

with a reason.

### Important Principle

Candidate selection and candidate scoring are separate processes.

Selection determines which compounds enter the research dataset.

Scoring will occur later and will use a predefined evidence-based comparison framework.
## 3. Candidate Selection Decision

### Final Candidate Set

The following 10 candidates have been selected for the initial TB research dataset:

| Candidate ID | Compound     | Selection Status |
| ------------ | ------------ | ---------------- |
| C-001        | Rifampicin   | INCLUDE          |
| C-002        | Isoniazid    | INCLUDE          |
| C-003        | Pyrazinamide | INCLUDE          |
| C-004        | Ethambutol   | INCLUDE          |
| C-005        | Bedaquiline  | INCLUDE          |
| C-006        | Delamanid    | INCLUDE          |
| C-007        | Pretomanid   | INCLUDE          |
| C-008        | Linezolid    | INCLUDE          |
| C-009        | Clofazimine  | INCLUDE          |
| C-010        | Sutezolid    | INCLUDE          |

### Selection Rationale

The candidates were selected to provide a scientifically useful mixture of established TB medicines, medicines important to drug-resistant TB treatment, and a newer investigational TB compound.

The selection is intended to provide variation in:

* Development stage
* Clinical evidence
* Regulatory evidence
* Biological evidence
* Literature availability
* Evidence completeness

The candidate list is not a ranking of therapeutic quality.

### Evidence Basis for Selection

WHO identifies rifampicin, isoniazid, pyrazinamide and ethambutol among the commonly used antibiotics for TB treatment.

WHO's current TB research and innovation information identifies bedaquiline and delamanid as drugs with accelerated regulatory approval, pretomanid as a drug approved by the U.S. FDA under a limited-population pathway, and sutezolid as one of the new chemical entities being studied in TB clinical development.

WHO TB treatment information also identifies medicines including bedaquiline, delamanid, linezolid and clofazimine in drug-resistant TB treatment contexts.

These facts establish relevance to the selected research area but do not establish that one candidate is clinically superior to another.

### Selection Status

Candidate list: FROZEN

Candidate evidence extraction: PENDING

Candidate comparison: PENDING

Evidence-gap analysis: PENDING
## 4. Candidate Dataset Schema

The candidate dataset uses a standardized CSV structure so that each candidate is evaluated using the same information fields.

### Required Fields

1. Candidate ID
2. Compound name
3. Synonyms
4. Source database
5. Molecular identifier
6. Target
7. Mechanism of action
8. Therapeutic area
9. Evidence stage
10. Potency
11. Selectivity
12. ADME
13. Safety/toxicity
14. Supporting publications
15. Known limitations
16. Evidence confidence
17. Missing information

### Data Entry Rules

* Each candidate must have a unique candidate ID.
* Compound names must be supported by an appropriate source.
* Molecular identifiers must be sourced rather than inferred.
* Scientific claims must be supported by appropriate evidence.
* Missing information must be recorded as `UNKNOWN / NOT FOUND`.
* Estimates and unsupported assumptions must not be entered as factual evidence.
* Different experimental measurements must not automatically be treated as directly comparable.
* Evidence source and analytical interpretation must remain distinguishable.

### Initial Dataset Status

The CSV contains the 10 frozen candidate IDs.

Detailed evidence extraction has not yet been completed.

Status: DATASET STRUCTURE INITIALIZED

