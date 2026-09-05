\# Phase 7 — Testing Plan



\## 1. Objective



The objective of Phase 7 is to verify that the Tuberculosis (TB) drug discovery research pipeline works correctly and produces consistent results.



\## 2. System Under Test



The main system being tested is the Python research pipeline created in Phase 5.



Main files:



\- candidate\_compounds.csv

\- drug\_discovery\_pipeline.py

\- calculate\_completeness.py



\## 3. Test Areas



The following areas will be tested:



1\. CSV loading

2\. Candidate search

3\. Synonym search

4\. Therapeutic-area filtering

5\. Evidence-stage filtering

6\. Candidate-detail display

7\. Invalid candidate handling

8\. Invalid menu input

9\. Empty search results

10\. Complete candidate listing

11\. CSV structure and data consistency



\## 4. Expected Dataset



Expected number of candidates:



10



Research area:



Tuberculosis (TB)



Candidate IDs:



C-001 to C-010



\## 5. Expected Evidence Stages



Approved candidates:



\- C-001

\- C-002

\- C-003

\- C-004

\- C-005

\- C-006

\- C-007

\- C-008

\- C-009



C-010 Sutezolid is not classified as Approved in the current dataset.



\## 6. Test Principle



Each test will compare the actual program output with the expected result.



A test is considered:



\*\*PASS\*\* — actual result matches expected result.



\*\*FAIL\*\* — actual result does not match expected result.



\## 7. Important Limitation



These tests verify software behavior and dataset structure.



They do not validate the clinical effectiveness, safety, or suitability of any drug.



\## 8. Phase 7 Status



Phase 7 Step 1:



\*\*COMPLETE\*\*

