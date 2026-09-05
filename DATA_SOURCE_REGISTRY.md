# Public Data Source Registry

## Purpose

This registry documents public biomedical and drug-discovery information sources that can support the New Drug Discovery Research Pipeline.

The purpose is to understand what information each source provides, how accessible it is, what formats are available, and what limitations should be considered when using the information for research.

A source containing information about a compound does not automatically establish that the compound is therapeutically validated.

Each source will therefore be evaluated according to:

* Organisation
* Purpose
* Data available
* Accessibility
* Data format
* Strengths
* Limitations
* Evidence quality
* Potential BHIV use
* Potential AI/Data Science use

## Source Evaluation Principles

1. Prefer authoritative and scientifically established sources.
2. Record what the source actually provides.
3. Do not treat database presence as proof of therapeutic effectiveness.
4. Distinguish primary evidence from database-derived information.
5. Record limitations and uncertainty.
6. Use multiple sources when important claims require verification.
7. Do not fill missing information with assumptions.
8. Maintain traceability between candidate information and its source.
## Source Overview

| ID     | Source             | Main Purpose                                    | Primary Use in Project                      |
| ------ | ------------------ | ----------------------------------------------- | ------------------------------------------- |
| DS-001 | PubChem            | Chemical and compound information               | Compound identity and molecular information |
| DS-002 | ChEMBL             | Bioactivity and drug-discovery data             | Bioactivity, targets and compound research  |
| DS-003 | PubMed             | Biomedical literature search                    | Scientific publications                     |
| DS-004 | Europe PMC         | Biomedical literature and related research data | Literature and publication discovery        |
| DS-005 | ClinicalTrials.gov | Clinical study registry                         | Clinical development evidence               |
| DS-006 | FDA                | Regulatory drug information                     | Approval and safety evidence                |
| DS-007 | Protein Data Bank  | 3D biological structure data                    | Target/structure research                   |
| DS-008 | WHO                | Global health and medicine resources            | Context and relevant health guidance        |

This table is an initial classification. Detailed source evaluation will be completed before the sources are used as evidence in the candidate registry.
## DS-001 — PubChem

### Organisation

U.S. National Library of Medicine (National Center for Biotechnology Information)

### Purpose

PubChem is a public chemical information resource that provides information about chemical substances and their biological activities.

### Data Available

Relevant data can include:

* Compound names
* Synonyms
* Chemical structures
* Molecular formula
* Molecular weight
* Chemical identifiers
* Bioassay information
* Links to related literature and resources

### Accessibility

Publicly accessible.

### Data Format

Information can be accessed through the PubChem web interface and programmatic/data-access mechanisms. Available formats depend on the specific resource or endpoint.

### Strengths

* Publicly accessible
* Large chemical-information resource
* Useful for compound identification
* Provides multiple identifiers and chemical properties
* Connects chemical information with biological and literature resources

### Limitations

* Presence of a compound record does not establish therapeutic effectiveness.
* Information may originate from different underlying sources and should be interpreted in context.
* Individual records may not contain all information required for drug-development assessment.
* Experimental results should be interpreted according to their assay and source context.

### Evidence Quality

High for basic compound identity and chemical information when the relevant record is authoritative and clearly documented.

For therapeutic effectiveness, safety, or clinical conclusions, additional appropriate sources should be consulted.

### Potential BHIV Use

PubChem can support the candidate compound registry by providing standardized compound identities, synonyms, molecular identifiers, and related chemical information.

### Potential AI/Data Science Use

PubChem data can support:

* Structured compound datasets
* Identifier normalization
* Data integration
* Candidate lookup
* Chemical-property analysis
* Future computational research

### Project Role

Primary supporting source for:

* Compound identity
* Synonyms
* Molecular identifiers
* Chemical information

It should not be treated as the sole source for therapeutic validation.
## DS-002 — ChEMBL

### Organisation

European Molecular Biology Laboratory — European Bioinformatics Institute (EMBL-EBI)

### Purpose

ChEMBL is a manually curated database of bioactive, drug-like molecules and their biological activities.

It is designed to support drug-discovery research by connecting chemical compounds with biological activity, targets, assays, and related information.

### Data Available

Relevant information can include:

* Compound information
* Chemical structures
* Molecular identifiers
* Biological targets
* Bioactivity measurements
* Assay information
* Activity types such as IC50, EC50, Ki and related measurements
* Publications associated with bioactivity data
* Drug and development information

### Accessibility

Publicly accessible.

ChEMBL provides web-based access and programmatic/data-access options.

### Data Format

Data can be accessed through the ChEMBL web interface, APIs, and downloadable database/data resources.

Available formats depend on the access method.

### Strengths

* Specifically designed for drug-discovery research
* Large collection of bioactivity data
* Connects compounds with biological targets
* Provides assay context for activity measurements
* Links activity information with scientific publications
* Useful for structured computational research

### Limitations

* Bioactivity measurements can come from different experimental systems.
* Values from different assays should not automatically be treated as directly comparable.
* A reported bioactivity measurement does not by itself establish clinical effectiveness.
* Database records may contain incomplete information for some compounds or targets.
* Biological activity must be interpreted in its experimental context.

### Evidence Quality

High for structured bioactivity information when the underlying record and experimental context are clearly documented.

However, individual measurements should be interpreted according to the assay, target, experimental system, and source publication.

ChEMBL data should not be treated as equivalent to clinical or regulatory evidence.

### Potential BHIV Use

ChEMBL can support:

* Candidate compound research
* Target-compound mapping
* Bioactivity evidence collection
* Potency-data extraction
* Candidate comparison
* Evidence-gap identification

### Potential AI/Data Science Use

ChEMBL can support:

* Structured bioactivity datasets
* Compound-target relationship analysis
* Data integration
* Machine-learning datasets
* Candidate prioritization research
* Bioactivity trend analysis
* Computational drug-discovery research

### Project Role

ChEMBL will be an important supporting source for:

* Target information
* Bioactivity information
* Potency measurements
* Assay context
* Publication-linked evidence

Important rule:

A ChEMBL activity record should be interpreted as evidence of a reported biological activity under a particular experimental context. It should not automatically be interpreted as proof of therapeutic effectiveness in humans.
## DS-003 — PubMed

### Organisation

U.S. National Library of Medicine (NLM), National Institutes of Health (NIH)

### Purpose

PubMed is a free resource for searching biomedical and life-sciences literature.

It is primarily used to discover scientific publications relevant to medicine, biology, pharmacology, drug discovery, and related fields.

### Data Available

Relevant information can include:

* Scientific publication citations
* Article titles
* Authors
* Journal information
* Publication dates
* Abstracts when available
* Medical subject headings (MeSH) and other indexing information
* Publication identifiers such as PMID
* Links to available full-text articles

### Accessibility

Publicly accessible for literature searching.

Access to the complete article may depend on the journal or external full-text provider.

### Data Format

Information can be accessed through the PubMed web interface and programmatic services.

The exact available data and format depend on the access method.

### Strengths

* Large biomedical literature database
* Maintained by a major biomedical information organization
* Useful for finding peer-reviewed scientific publications
* Supports searches by topic, author, publication, and biomedical concepts
* Provides publication identifiers that improve evidence traceability
* Useful for finding primary research and review articles

### Limitations

* PubMed primarily provides literature records rather than being a complete compound database.
* An abstract may not contain all experimental details.
* Some full-text articles may not be freely accessible.
* A publication appearing in PubMed does not automatically mean that its conclusions are strong or applicable to every research question.
* Different studies may report different results or use different experimental methods.

### Evidence Quality

Potentially high for locating scientific evidence, particularly when the underlying publication is a relevant primary research study.

The quality of evidence must be assessed at the individual publication level.

A PubMed record itself should not automatically be interpreted as proof of a scientific claim.

### Potential BHIV Use

PubMed can support:

* Biomedical literature research
* Candidate compound evidence collection
* Target and mechanism research
* Potency evidence research
* Safety/toxicity research
* Evidence-gap analysis
* Literature traceability

### Potential AI/Data Science Use

PubMed can support:

* Literature retrieval
* Publication metadata datasets
* Natural-language processing
* Literature classification
* Evidence extraction
* Relationship mapping between compounds, targets, diseases, and publications
* Future biomedical research systems

### Project Role

PubMed will primarily be used to locate supporting scientific publications for candidate compounds and their properties.

Important rule:

The existence of a PubMed publication does not automatically establish that the compound is effective, safe, or clinically superior. The actual study must be examined to determine what evidence it provides.
## DS-004 — Europe PMC

### Organisation

Europe PMC is operated by EMBL-EBI (European Bioinformatics Institute) and supported by Europe PMC funders.

### Purpose

Europe PMC is a public biomedical literature and research information resource.

It provides access to scientific publications and related biomedical research information, with tools that support literature discovery, linking, and programmatic access.

### Data Available

Relevant information can include:

* Scientific publications
* Article titles
* Authors
* Abstracts
* Publication dates
* Journal information
* Publication identifiers
* Links to full-text articles when available
* References and related articles
* Research-related metadata
* Some links to associated research information

### Accessibility

Publicly accessible.

Europe PMC provides web-based search and programmatic access.

### Data Format

Information can be accessed through the Europe PMC website, APIs, and downloadable resources.

Available formats depend on the specific service or endpoint.

### Strengths

* Large biomedical literature resource
* Useful for literature discovery
* Provides access to abstracts and, where available, full-text content
* Provides programmatic access suitable for data analysis
* Links publications with related research information
* Useful for discovering relationships between publications and biomedical entities
* Can complement PubMed searches

### Limitations

* Not every publication is freely available in full text.
* Literature records vary in completeness.
* The presence of a publication does not establish that its conclusions are correct or clinically applicable.
* Different studies may use different experimental systems and methods.
* Literature information must be interpreted in the context of the original study.

### Evidence Quality

Potentially high for locating relevant scientific literature.

The evidence quality must ultimately be assessed from the individual publication and study design rather than from the existence of a record in Europe PMC.

### Potential BHIV Use

Europe PMC can support:

* Biomedical literature discovery
* Candidate compound research
* Target and mechanism research
* Evidence-gap analysis
* Publication tracking
* Cross-referencing scientific evidence

### Potential AI/Data Science Use

Europe PMC can support:

* Literature datasets
* Natural-language processing
* Biomedical entity extraction
* Literature classification
* Evidence retrieval
* Relationship analysis between compounds, diseases, targets, and publications
* Future biomedical AI research

### Project Role

Europe PMC will be used as a complementary literature source for identifying scientific publications and research evidence related to candidate compounds, targets, mechanisms, potency, ADME, and safety.

Important rule:

Europe PMC is a literature discovery and research-information resource. A publication record alone does not prove therapeutic effectiveness or clinical superiority.
## DS-005 — ClinicalTrials.gov

### Organisation

ClinicalTrials.gov is maintained by the U.S. National Library of Medicine (NLM), part of the National Institutes of Health (NIH).

### Purpose

ClinicalTrials.gov is a public registry and results database for clinical studies.

It provides information about clinical studies involving human participants and helps researchers and the public find information about ongoing, completed, and registered studies.

### Data Available

Relevant information can include:

* Study title
* Study identification number
* Study type
* Study status
* Conditions studied
* Interventions
* Study design
* Eligibility criteria
* Participant information
* Sponsor information
* Study locations
* Outcome measures
* Results information when available
* Publication and related information when available

### Accessibility

Publicly accessible through the ClinicalTrials.gov website and data-access mechanisms.

### Data Format

Information is available through the web interface and structured data/programmatic access options.

Available formats depend on the particular access method.

### Strengths

* Public clinical-study registry
* Useful for identifying human studies
* Provides structured study information
* Allows investigation of study status and design
* Useful for tracking clinical development
* Provides information that can complement scientific publications

### Limitations

* Registration of a clinical study does not prove that the intervention was effective.
* Not every registered study has publicly available results.
* Study records can change over time.
* Registered information may be incomplete.
* A clinical trial record must be interpreted according to its study design, population, intervention, endpoints, and status.
* ClinicalTrials.gov should not be treated as a substitute for regulatory approval information.

### Evidence Quality

High for determining whether a registered clinical study exists and for examining the information contained in the registry record.

Evidence about effectiveness requires appropriate interpretation of the study results and design.

### Potential BHIV Use

ClinicalTrials.gov can support:

* Clinical development-stage assessment
* Identification of human studies
* Candidate development tracking
* Evidence-gap analysis
* Clinical research mapping

### Potential AI/Data Science Use

ClinicalTrials.gov data can support:

* Clinical-trial datasets
* Trial-status analysis
* Study classification
* Clinical research trend analysis
* Intervention-condition relationship mapping
* Research prioritization systems

### Project Role

ClinicalTrials.gov will primarily support assessment of clinical-development evidence for candidate compounds.

It can help determine whether a candidate has been investigated in human clinical studies and what information is available about those studies.

Important rule:

"Clinical trial registered" must not be interpreted as "clinically proven."

A registered study is evidence that a study exists or existed under the information recorded in the registry. Conclusions about effectiveness require examination of the study design and results.
## DS-006 — U.S. Food and Drug Administration (FDA)

### Organisation

U.S. Food and Drug Administration (FDA), United States Department of Health and Human Services.

### Purpose

The FDA is a U.S. regulatory authority responsible for protecting public health by regulating products including drugs and biologics.

For this project, FDA resources can provide regulatory and safety information about medicines and drug products.

### Data Available

Depending on the specific FDA resource or document, information can include:

* Approved indications
* Prescribing information
* Dosage and administration information
* Contraindications
* Warnings and precautions
* Adverse reactions
* Clinical-study information
* Pharmacokinetic information
* Drug labeling
* Regulatory information

### Accessibility

Many FDA drug-information resources and regulatory documents are publicly accessible.

### Data Format

Information may be available through:

* FDA webpages
* Drug labels
* Regulatory documents
* Structured or downloadable resources where provided

The available format depends on the specific FDA resource.

### Strengths

* Authoritative regulatory source
* Useful for approved drug information
* Provides important safety and warning information
* Provides official product-label information
* Useful for understanding regulatory status
* Can provide clinical and pharmacokinetic information for approved products

### Limitations

* FDA information is primarily relevant to products and indications within the regulatory context of the document.
* Not every research compound has FDA information.
* Regulatory documents should not be generalized beyond the specific product, formulation, indication, or population described.
* FDA approval does not mean a drug is free from adverse effects.
* An FDA source should not be used to claim that one approved drug is universally superior to another.

### Evidence Quality

High for regulatory claims directly supported by official FDA documents.

Examples include:

* Regulatory status
* Approved indications
* Official warnings
* Contraindications
* Label-based safety information

### Potential BHIV Use

FDA resources can support:

* Regulatory-status verification
* Safety evidence
* Approved-indication verification
* Pharmacokinetic evidence
* Candidate evidence comparison
* Evidence-gap analysis

### Potential AI/Data Science Use

FDA information can support:

* Regulatory-status datasets
* Drug-label extraction
* Safety-information extraction
* Natural-language processing
* Structured regulatory evidence
* Drug safety and development research

### Project Role

FDA resources will primarily be used to verify regulatory and safety information for candidates where official FDA documentation is available.

Important rule:

FDA evidence should be linked to the specific product, indication, formulation, and regulatory document being examined. FDA approval or regulatory documentation should not automatically be interpreted as proof that a compound is clinically superior to other candidates.
## DS-007 — Protein Data Bank (PDB)

### Organisation

The Protein Data Bank (PDB) is an international public resource for three-dimensional structural information about biological macromolecules. The worldwide Protein Data Bank (wwPDB) organization coordinates the PDB archive through its member organizations.

### Purpose

The Protein Data Bank provides experimentally determined three-dimensional structures of biological macromolecules and their complexes.

In drug-discovery research, structural information can help researchers investigate biological targets and molecular interactions.

### Data Available

Relevant information can include:

* Three-dimensional structures of proteins and other biological macromolecules
* Protein-ligand complex structures
* Molecular coordinates
* Structural metadata
* Experimental method information
* Resolution information for relevant structures
* Ligand information
* Links to related structural and scientific information

### Accessibility

Publicly accessible.

PDB structures and associated information can be accessed through public web resources and data-download mechanisms.

### Data Format

Structural data are available in standardized structural-data formats, including PDB and mmCIF-related formats.

The exact available format depends on the structure and access method.

### Strengths

* Major public source of biological macromolecular structures
* Provides three-dimensional structural information
* Useful for studying protein-ligand interactions
* Useful for understanding potential binding sites
* Can support structural biology and computational drug-discovery research
* Provides experimental-method and structural metadata

### Limitations

* A structure may not exist for every biological target or compound.
* Structural information does not automatically prove therapeutic effectiveness.
* A protein-ligand structure does not by itself establish clinical benefit.
* Structures may differ in experimental conditions, resolution, construct, ligand state, or biological context.
* Structural evidence should be interpreted together with biochemical, cellular, clinical, and other relevant evidence.

### Evidence Quality

High for the structural information directly represented by a deposited structure and its associated experimental metadata.

Structural evidence should not automatically be interpreted as evidence of clinical effectiveness.

### Potential BHIV Use

PDB can support:

* Target structure research
* Protein-ligand interaction research
* Binding-site investigation
* Candidate compound analysis
* Structural evidence collection
* Future computational drug-discovery research

### Potential AI/Data Science Use

PDB data can support:

* Protein-structure datasets
* Structural feature extraction
* Protein-ligand relationship analysis
* Molecular modeling research
* Computational drug discovery
* Machine-learning research involving molecular structures

### Project Role

PDB will be used as a supporting structural source when relevant structures exist for a candidate's molecular target or target-compound complex.

Important rule:

The presence of a protein-ligand structure does not by itself prove that the compound is therapeutically effective, safe, or clinically superior.
## DS-008 — World Health Organization (WHO)

### Organisation

World Health Organization (WHO)

### Purpose

WHO provides international health guidance, standards, technical resources, and information related to medicines and health products.

WHO resources can support research into medicines, essential medicines, pharmaceutical quality, regulation, safety, and global health priorities.

### Data Available

Depending on the specific WHO resource, relevant information can include:

* WHO Model List of Essential Medicines
* International Nonproprietary Names (INN)
* Pharmaceutical standards and guidance
* Medicines and health-product policies
* Regulatory and quality-related resources
* Medicine-related databases and tools
* Global health information
* Technical reports and publications
* Information related to medicine safety and access

### Accessibility

Publicly accessible through WHO websites, publications, databases, and technical resources.

### Data Format

Information may be available through:

* Web pages
* Reports
* Guidelines
* Publications
* Databases
* Downloadable documents

The format depends on the specific WHO resource.

### Strengths

* Internationally recognized health organization
* Provides authoritative health and medicines guidance
* Useful for global medicines policy and standards
* Provides the WHO Model List of Essential Medicines
* Provides pharmaceutical and health-product guidance
* Useful for understanding global health priorities and medicine access

### Limitations

* WHO is not primarily a compound bioactivity database.
* WHO resources may not contain detailed experimental data for individual candidate compounds.
* Inclusion in a WHO list or resource does not automatically mean that a compound is superior to other medicines.
* WHO resources should be interpreted according to the purpose and scope of the specific document or database.

### Evidence Quality

High for WHO recommendations, standards, classifications, and information directly published by WHO.

The relevance of the evidence depends on the specific WHO resource being used.

WHO information should not be used as a substitute for detailed compound-level experimental evidence when such evidence is required.

### Potential BHIV Use

WHO resources can support:

* Therapeutic-area context
* Essential-medicine status
* Medicine policy research
* Global health context
* Regulatory and quality research
* Evidence-gap analysis
* Understanding medicine access and public-health relevance

### Potential AI/Data Science Use

WHO resources can support:

* Structured medicine datasets
* Medicine classification
* Global health-data analysis
* Natural-language processing of guidelines and reports
* Health-policy research
* Medicine-access analysis

### Project Role

WHO will be used as a contextual and supporting source where relevant to candidate compounds, therapeutic areas, medicine classification, essential-medicine status, pharmaceutical standards, or global health considerations.

Important rule:

WHO information should be interpreted according to the specific resource being used. Inclusion in a WHO resource does not automatically establish that a candidate is clinically superior or suitable for development.
# 11. Source-to-Data Mapping

The candidate-compound registry will use different sources for different types of evidence.

No single source will be treated as sufficient for every candidate field.

| Candidate Field         | Primary Source(s)               | Supporting Source(s)          |
| ----------------------- | ------------------------------- | ----------------------------- |
| Candidate ID            | Project registry                | —                             |
| Compound name           | PubChem                         | ChEMBL                        |
| Synonyms                | PubChem                         | ChEMBL                        |
| Molecular identifier    | PubChem                         | ChEMBL                        |
| Target                  | ChEMBL                          | PubMed, PDB                   |
| Mechanism of action     | PubMed                          | ChEMBL, FDA where applicable  |
| Therapeutic area        | PubMed                          | ClinicalTrials.gov, FDA       |
| Evidence stage          | ClinicalTrials.gov, FDA         | ChEMBL, PubMed                |
| Potency                 | ChEMBL                          | Primary research publications |
| Selectivity             | ChEMBL                          | Primary research publications |
| ADME                    | FDA where available             | PubMed, primary research      |
| Safety/toxicity         | FDA where available             | PubMed, ClinicalTrials.gov    |
| Supporting publications | PubMed                          | Europe PMC                    |
| Structural evidence     | PDB                             | PubMed                        |
| Known limitations       | PubMed, FDA, ClinicalTrials.gov | ChEMBL, Europe PMC            |
| Evidence confidence     | Combined source assessment      | All relevant sources          |

## Source Selection Rules

### Rule 1 — Use the source appropriate to the question

Different sources provide different types of evidence.

Example:

A chemical identifier should preferably be obtained from a chemical-information source rather than inferred from a scientific article.

### Rule 2 — Prefer direct evidence

When a primary research publication directly reports an experimental result, the publication should be considered when recording that result.

### Rule 3 — Preserve experimental context

Potency and bioactivity measurements should be recorded together with relevant assay or experimental context when available.

Different measurements should not automatically be treated as directly comparable.

### Rule 4 — Regulatory claims require regulatory evidence

Claims about approval, approved indications, warnings, or official regulatory status should preferably be supported by an appropriate regulatory source.

### Rule 5 — Clinical claims require clinical evidence

A compound's presence in a clinical-trial registry does not prove effectiveness.

Clinical-study status, design, and results must be examined separately.

### Rule 6 — Structural evidence is not clinical evidence

A protein-ligand structure can provide structural information about molecular interactions, but it does not by itself establish therapeutic effectiveness or safety.

### Rule 7 — Missing information remains UNKNOWN / NOT FOUND

If appropriate sources do not provide reliable information for a required field, the candidate registry will contain:

UNKNOWN / NOT FOUND

No value will be invented or estimated without an appropriate evidence basis.

## Evidence Traceability

Each important candidate property should be traceable to one or more sources.

The intended evidence chain is:

Public source
→ specific record/publication
→ extracted information
→ candidate registry field
→ evidence confidence
→ comparison
→ evidence-gap analysis

## Evidence vs Analysis

The candidate registry will contain evidence collected from sources.

The candidate comparison will contain analytical scoring based on predefined rules.

These two layers must remain separate.

A higher analytical score means:

"Stronger documented evidence according to the project's scoring framework."

It does not mean:

"Clinically superior drug."
