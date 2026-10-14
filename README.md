# Clinical WES/WGS Variant Interpretation and Prioritization: An Evidence-Based Framework for Resource Selection and Integration

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Catalog version](https://img.shields.io/badge/catalog-v0.3.0-blue.svg)](CHANGELOG.md)
[![Validate catalog](https://github.com/timt-web/WER-KB/actions/workflows/validate.yml/badge.svg)](https://github.com/timt-web/WER-KB/actions/workflows/validate.yml)

WER-KB is the updateable implementation and documentation layer for this framework. It links each representative resource to its analytical purpose, evidence type, workflow position, population and clinical relevance, input and output characteristics, genome-build and transcript compatibility, maintenance, version or release, key limitations, complementary resources, and supporting citation.

The catalog covers post-analytical interpretation and prioritization of germline single-nucleotide variants and small insertions/deletions identified through clinical WES/WGS. Resources are representative as opposed to mandatory.

## Citation

Please cite the manuscript:

> Clinical WES/WGS Variant Interpretation and Prioritization: An Evidence-Based Framework for Resource Selection and Integration.

Until a DOI is available, also cite this repository:

> WER-KB contributors. WER-KB (v0.3.0). https://github.com/timt-web/WER-KB

[`CITATION.cff`](CITATION.cff) is included so GitHub can format the repository citation. If you rely on a particular snapshot, name the release tag and commit.

## Scope

The framework organizes resource selection and evidence integration. It does not replace a laboratory pipeline, the ACMG/AMP criteria, an applicable ClinGen specification, or expert judgment. Computational and AI-assisted methods are supportive rather than standalone determinants of clinical classification or clinical decision-making.

Copy-number variants, structural variants, repeat expansions, mitochondrial variants, mosaic variants, somatic variants, and pharmacogenomic associations are outside this scope. WER-KB is not a clinically validated decision-support system.

## Workflow

The same 11 stages are written out with their representative resources in [`docs/workflow.md`](docs/workflow.md).

1. **Variant quality assessment and filtering.** Is the variant call of sufficient quality for post-analytical interpretation? Pipeline- and parameter-dependent.
2. **Variant quality assessment and filtering.** Which variants remain after documented filtering? Pipeline- and parameter-dependent. Filtering does not establish pathogenicity.
3. **Genome and transcript annotation.** Which genome build, gene, transcript, and molecular consequence apply to this variant? Transcript and genome-build discrepancies.
4. **Population-frequency assessment.** Is the population frequency compatible with the disease model and the ancestry of the individual? Population representation and ancestry bias; rarity alone does not establish pathogenicity.
5. **Phenotype- and gene-based prioritization.** Which genes or variants show phenotype–gene matching for the recorded phenotype and the mode of inheritance? Incomplete, nonspecific, or inaccurately captured phenotypes. Phenotypic concordance does not establish causality.
6. **Gene–disease evaluation.** What is the gene–disease validity and clinical relevance for this indication? Evidence is evolving and may vary in strength and curation status.
7. **Functional and computational assessment.** Which computational predictions, regulatory and expression observations, or protein-structure and protein-function observations apply to this variant? Computational outputs are supportive rather than standalone determinants of clinical classification.
8. **Splicing assessment.** Could this variant alter splicing of a clinically relevant transcript? Tissue, transcript, and context dependence.
9. **Evidence integration.** Which functional, clinical, and literature-based observations are relevant, and which of them share underlying datasets, annotations, or publications? Conflicting, heterogeneous, or incompletely curated evidence.
10. **Clinical variant classification.** Which ACMG/AMP criteria and ClinGen specifications apply after the evidence has been appraised? Requires contextual assessment and expert review.
11. **Reporting and reinterpretation.** What resource identities, versions, evidence, and limitations must be documented for clinical reporting and later reinterpretation? Evidence and interpretations may change over time.

## Using an entry

Start from the analytical question, then read the entries whose evidence type fits the case. Notes on why each resource was included are in [`docs/resource_selection_rationales.md`](docs/resource_selection_rationales.md).

When a resource is used, record its identity and version, the reference genome and transcript model, the filtering criteria, the evidence sources, the applicable clinical specifications, the key limitations, and the rationale for resource selection. A population frequency, a computational score, a phenotype–gene rank, or a database assertion answers only the analytical purpose recorded for that resource. Clinical variant classification still uses the ACMG/AMP criteria and any applicable ClinGen specification, with contextual assessment and expert review.

Agreement among resources is not independent evidence when they share datasets, annotations, publications, training data, or modelling assumptions.

## Files

| Path | What it is |
|---|---|
| [`data/resource_catalog.csv`](data/resource_catalog.csv) | The catalog. Edit this when a resource changes. |
| [`data/workflow_mapping.csv`](data/workflow_mapping.csv) | Stage names, analytical questions, and key limitations. |
| [`data/resource_dependencies.csv`](data/resource_dependencies.csv) | Where resources may share data, training material, or papers. |
| [`data/resource_catalog.json`](data/resource_catalog.json) | The same catalog in JSON. Schema: [`schemas/resource_catalog.schema.json`](schemas/resource_catalog.schema.json). |
| [`docs/workflow.md`](docs/workflow.md) | The 11 stages with their representative resources. |
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

WER-KB is an updatable research resource for methods work. It is not medical advice, and it is not a basis on its own for a diagnosis or for managing a patient.

## License

[MIT](LICENSE). Copyright (c) 2026 WER-KB contributors.
