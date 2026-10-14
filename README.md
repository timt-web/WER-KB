# An evidence-based knowledge base for clinical WES/WGS variant interpretation and prioritization

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Catalog version](https://img.shields.io/badge/catalog-v0.2.0-blue.svg)](CHANGELOG.md)
[![Validate catalog](https://github.com/timt-web/WER-KB/actions/workflows/validate.yml/badge.svg)](https://github.com/timt-web/WER-KB/actions/workflows/validate.yml)

WER-KB is the resource catalog for this paper. It covers the part of clinical exome and genome analysis that starts after variant calling: which databases, tools, and guidelines a laboratory might consult for a germline single-nucleotide variant or small indel, and what each of those outputs can and cannot decide.

The list is selective. A resource is included for a defined question in that work, together with the main limit on its use. Inclusion is not a recommendation to run it in every case.

## Citation

Please cite the manuscript:

> An evidence-based knowledge base for clinical WES/WGS variant interpretation and prioritization.

Until a DOI is available, also cite this repository:

> WER-KB contributors. WER-KB (v0.2.0). https://github.com/timt-web/WER-KB

[`CITATION.cff`](CITATION.cff) is included so GitHub can format the repository citation. If you rely on a particular snapshot, name the release tag and commit.

## Scope

The catalog is about post-analytical interpretation of germline SNVs and small indels from clinical whole-exome or whole-genome sequencing. That includes choosing a resource, reading its evidence, prioritizing candidates, supporting classification, writing the record, and deciding when to look again.

It is not a pipeline, a required tool list, a clinically validated decision-support system, or an automated classifier. It also does not replace a validated laboratory procedure, the ACMG/AMP criteria, an applicable ClinGen specification, local governance, or review by someone qualified to sign out the case.

## Workflow

The same 11 stages are written out with their resources in [`docs/workflow.md`](docs/workflow.md). The short form is the question, then the limit.

1. **Variant-level quality review.** Are the post-calling quality metrics and the call itself plausible for interpretation? Technical outputs are pipeline and parameter dependent.
2. **Variant-level filtering.** Which variants remain after documented, case-appropriate filters and normalization? Filtering does not establish pathogenicity.
3. **Genome and transcript annotation.** Which genome build, gene, transcript, and molecular consequence apply to this variant? Transcript selection and release differences can alter interpretation.
4. **Population-frequency assessment.** Is the observed allele frequency compatible with the proposed disease model and ancestry context? Rarity alone does not establish pathogenicity.
5. **Phenotype- and gene-based prioritization.** Which genes or variants rank highest given the structured phenotype and the inheritance context? Prioritization is not proof of causality.
6. **Gene–disease association assessment.** How strong is the gene–disease relationship for this clinical question? Curation coverage and strength vary.
7. **Computational variant-effect assessment.** Which computational, regulatory, or protein-level observations apply to this variant class? Predictions and annotations are supportive, not autonomous clinical evidence.
8. **Splicing assessment.** Could this variant alter splicing of a clinically relevant transcript? Predicted splice effects require contextual and, where possible, experimental corroboration.
9. **Functional, clinical, and literature evidence integration.** Which functional, clinical, and literature observations are relevant, and which of them repeat the same underlying data? A collected set of observations does not establish pathogenicity, and sources that share underlying data do not provide independent confirmation.
10. **ACMG/AMP-based classification.** Which ACMG/AMP criteria and ClinGen specifications apply after the evidence has been appraised? Automated support tools do not replace contextual expert classification.
11. **Reporting, documentation, and reinterpretation.** What resources, versions, evidence, decisions, and limitations must the report preserve for later reinterpretation? Evidence and interpretations may change over time.

## Using an entry

Start from the question, not from a favourite tool. Match it to a stage, then read the entries whose evidence type fits the case. Notes on why each resource was included are in [`docs/resource_selection_rationales.md`](docs/resource_selection_rationales.md).

When you use one, write down the release, the date you looked, the genome build, the transcript, what you put in, what you got back, and what you decided. Ask where the data came from, whether the method fits the variant class, and whether another source you are using is really the same evidence under a different name.

A frequency, a score, a phenotype rank, or a database assertion answers only the question recorded for that resource. Classification still goes through the ACMG/AMP criteria, any ClinGen specification that applies, the laboratory procedure, and someone who can review the case.

## Files

| Path | What it is |
|---|---|
| [`data/resource_catalog.csv`](data/resource_catalog.csv) | The catalog. Edit this when a resource changes. |
| [`data/workflow_mapping.csv`](data/workflow_mapping.csv) | Stage names, questions, and limits. |
| [`data/resource_dependencies.csv`](data/resource_dependencies.csv) | Where resources may share data, training material, or papers. |
| [`data/resource_catalog.json`](data/resource_catalog.json) | The same catalog in JSON. Schema: [`schemas/resource_catalog.schema.json`](schemas/resource_catalog.schema.json). |
| [`docs/workflow.md`](docs/workflow.md) | The 11 stages with their resources. |
| [`docs/resource_selection_rationales.md`](docs/resource_selection_rationales.md) | A short note on each resource. |
| [`schemas/resource_catalog_schema.md`](schemas/resource_catalog_schema.md) | Field definitions and allowed values. |
| [`docs/governance.md`](docs/governance.md) | How entries are added, reviewed, and retired. |
| [`docs/contribution_guide.md`](docs/contribution_guide.md) | How to propose a change. |

After a change to the tables, refresh the JSON and the two docs, then check them:

```bash
python3 scripts/build_catalog.py
python3 scripts/validate_catalog.py
```

Before a release, also run `python3 scripts/check_urls.py`. An HTTP 403 from that check means the site blocked the script; it does not by itself mean the page is gone. The validator also runs on pull requests.

## Disclaimer

WER-KB is for research, teaching, and methods work. It is not medical advice, and it is not a basis on its own for a diagnosis or for managing a patient.

## License

[MIT](LICENSE). Copyright (c) 2026 WER-KB contributors.
