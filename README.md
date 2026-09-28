# WER-KB

## An evidence-based knowledge base for clinical WES/WGS variant interpretation and prioritization

WER-KB is an updateable, versioned resource catalog that operationalizes the framework described in **“An Evidence-Based Framework for Clinical WES/WGS Variant Interpretation and Prioritization.”** It supports transparent selection and contextual interpretation of databases, tools, guidelines, and knowledge resources used after candidate variants have been generated.

## Scope

WER-KB focuses on post-analytical interpretation of germline single-nucleotide variants and small insertions/deletions identified through clinical whole-exome or whole-genome sequencing. It supports resource selection, evidence appraisal, candidate prioritization, formal classification support, documentation, and reinterpretation.

It is not:

- A fixed pipeline or mandatory tool list.
- A clinically validated decision-support system.
- An automated classifier.
- A substitute for validated laboratory workflows, ACMG/AMP criteria, applicable ClinGen specifications, clinical governance, or expert judgment.

## Core principle

Resources are included as **representative, context-appropriate options**, not universal requirements. Each entry records what question a resource addresses, why it is included, when it may be appropriate, what its output cannot establish alone, and its principal limitations and dependencies.

## Repository layout

- `data/resource_catalog.csv` — primary, machine-readable catalog of core representative resources.
- `data/resource_catalog.json` — JSON mirror of the catalog.
- `data/workflow_mapping.csv` — 11-stage post-analytical workflow mapping.
- `data/resource_dependencies.csv` — common dependency and non-independence considerations.
- `docs/resource_selection_rationales.md` — readable rationale entries for all resources.
- `docs/governance.md` — inclusion, review, update, and retirement policy.
- `docs/contribution_guide.md` — instructions for proposing additions or updates.
- `schemas/resource_catalog_schema.md` — field definitions and controlled vocabulary.
- `templates/resource_entry_template.md` — entry template for new resources.
- `CHANGELOG.md` — release history.

## Workflow stages

1. Variant-level quality review
2. Variant-level filtering
3. Genome and transcript annotation
4. Population-frequency assessment
5. Phenotype- and gene-based prioritization
6. Gene–disease association assessment
7. Computational variant-effect assessment
8. Splicing assessment
9. Functional, clinical, and literature evidence integration
10. ACMG/AMP-based classification
11. Reporting, documentation, and reinterpretation

## Use guidance

1. Define the analytical question.
2. Select only resources that address that question in the case context.
3. Record resource version/release, access date, genome build, transcript model, inputs, outputs, and key decisions.
4. Assess provenance, methodological quality, biological relevance, clinical applicability, and possible dependence among sources.
5. Do not infer pathogenicity, causality, or diagnostic relevance from a single database entry, prediction score, or phenotype ranking.
6. Apply formal clinical classification using applicable ACMG/AMP criteria, relevant specifications, validated laboratory procedures, and expert review.

## Citation

If you use WER-KB, cite the associated manuscript once bibliographic details are available. Until then, cite this repository by release tag and commit hash.

## License and disclaimer

This repository is intended for research, educational, and framework-development purposes. It is not medical advice and must not be used as a stand-alone basis for clinical diagnosis or patient management. Adopt an explicit license before public release.
