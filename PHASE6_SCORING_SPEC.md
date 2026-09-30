# Phase 6 Scoring Specification

## Purpose

The scoring system provides a deterministic comparison of TB drug-discovery candidates using documented evidence and predefined comparison dimensions.

The score is a decision-support output and does not represent scientific truth, clinical efficacy, safety, regulatory approval, or overall drug quality.

## Scoring Dimensions

The total score is calculated using eight dimensions.

1. Target Relevance
2. Mechanism Evidence
3. Potency Evidence
4. Selectivity Evidence
5. ADME Evidence
6. Safety Evidence
7. Research and Development Evidence
8. Evidence Completeness

## Maximum Score

Each dimension has a maximum value of 5.

Maximum total score:

40

Formula:

Total Score =
Target Relevance
+ Mechanism Evidence
+ Potency Evidence
+ Selectivity Evidence
+ ADME Evidence
+ Safety Evidence
+ Research and Development Evidence
+ Evidence Completeness

## Score Range

Minimum score: 0

Maximum score: 40

## Normalization

All scoring dimensions use the same 0–5 scale.

0 = No usable evidence

1 = Very limited evidence

2 = Limited evidence

3 = Moderate evidence

4 = Strong evidence

5 = Very strong documented evidence

The score represents the strength or completeness of the available evidence for the specified comparison dimension.

## Missing Data Treatment

Missing evidence must not automatically be interpreted as negative scientific evidence.

If a required score input is unavailable, the system should identify the missing input through the evidence-gap system.

A missing score input must remain distinguishable from a documented low score.

## Source Evidence Boundary

Primary and source evidence must remain separate from derived comparison scores.

Examples of source evidence include:

- Target information
- Mechanism information
- Potency information
- Selectivity information
- ADME information
- Safety information
- Supporting publications
- Development-stage information

Scores are derived outputs based on these evidence fields.

## Deterministic Requirement

The scoring process must be deterministic.

The same candidate data and the same scoring method must produce the same score and comparison result on repeated execution.

## Reproducibility

Repeated execution with unchanged input must produce:

- identical dimension scores
- identical total scores
- identical ranking order
- identical candidate identifiers
- identical output structure

## Tie Handling

Candidates with identical total scores retain a deterministic ordering based on candidate ID.

This prevents execution order from changing the comparison output.

## Current Scoring Results

| Rank | Candidate ID | Compound | Score |
|---:|---|---|---:|
| 1 | C-002 | Isoniazid | 34/40 |
| 2 | C-005 | Bedaquiline | 32/40 |
| 3 | C-001 | Rifampicin | 30/40 |
| 4 | C-008 | Linezolid | 30/40 |
| 5 | C-004 | Ethambutol | 29/40 |
| 6 | C-006 | Delamanid | 29/40 |
| 7 | C-007 | Pretomanid | 29/40 |
| 8 | C-003 | Pyrazinamide | 28/40 |
| 9 | C-009 | Clofazimine | 25/40 |
| 10 | C-010 | Sutezolid | 24/40 |

These scores are derived comparison outputs from the existing scoring implementation.

They must not be interpreted as clinical recommendations, efficacy rankings, regulatory decisions, or scientific truth.

## Limitations

The scoring system depends on the quality, completeness, and structure of the underlying evidence.

The score does not replace:

- scientific review
- clinical evaluation
- toxicology assessment
- regulatory assessment
- expert judgment
- systematic literature review

An evidence gap does not mean that the candidate is ineffective or unsafe.

A higher derived score does not establish that a candidate is clinically superior.

## Phase 6 Requirements

The implementation must support:

- deterministic scoring
- documented scoring inputs
- reproducible results
- explicit missing-data handling
- deterministic tie handling
- separation of evidence and derived scores
- structured comparison output
- score provenance
- score method versioning