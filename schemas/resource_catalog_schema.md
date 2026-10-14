# Resource catalog schema

The catalog is kept in `data/resource_catalog.csv`. The JSON file, the rationale notes, and the resource lists in the workflow follow that table. `scripts/validate_catalog.py` checks entries against this schema.

## Required fields

| Field | Definition | Allowed/expected values |
|---|---|---|
| `resource_id` | Stable machine-readable identifier | lowercase kebab-case, unique |
| `resource_name` | Public resource name | unique text |
| `resource_class` | Resource category | tool; database; predictor; ontology; guideline; curation resource; reference |
| `analytical_function` | Role in the framework | one or more of the 13 functions below, separated by `;` |
| `workflow_stages` | Applicable stages | unique integers from 1 to 11, ascending, separated by `;` |
| `evidence_type` | Nature of the output | one value from the evidence-type list below |
| `primary_purpose` | Defined analytical purpose | concise text |
| `input` | Expected input | concise text |
| `output` | Produced information | concise text |
| `genome_build_compatibility` | Genome-build context | one or more build tokens below, in the listed order, separated by `;` |
| `technical_compatibility` | Interfaces, formats, and other technical constraints | concise text |
| `maintenance_status` | Maintenance state | one value from the maintenance list below |
| `selection_rationale` | Why it is included | concise, auditable text |
| `appropriate_use` | Situations in which it may be appropriate | concise text |
| `interpretation_boundary` | Inferences that must not be made from the output alone | concise text |
| `key_limitations` | Material limitations and biases | concise text |
| `complementary_resources` | Other catalogued resources that add distinct context | `resource_id` values separated by `;`; may be empty |
| `complementary_context` | Non-catalogued context that should be considered with the output | concise text; may be empty |
| `official_url` | Page that identifies this resource | absolute `http` or `https` URL |
| `supporting_citation` | Supporting publication or official documentation | citation recorded in the manuscript; required |
| `version_or_release` | Release checked for this catalog entry | a release, a dated document, or `not recorded` |
| `reverify_at_use` | Whether the release must be checked again at the point of use | `yes`; `no` |
| `access_date` | Date the entry was checked | ISO 8601 date |
| `status` | Catalog status | core representative resource; candidate; retired; out of scope |

`version_or_release` records the release this review actually identified. Use `not recorded` when that review did not capture a release identifier. `not recorded` requires `reverify_at_use` = `yes`. Do not use a placeholder such as "To be confirmed at use" in place of either field.

`reverify_at_use` = `no` is appropriate only when `version_or_release` cites a fixed document or data release.

## Analytical functions

Names follow Table 1.

1. Variant-Level Quality Control & Filtering
2. Genome & Transcript Annotation
3. Population & Frequency
4. Phenotype & Gene Prioritization
5. Gene–Disease Association
6. Computational Variant-Effect Prediction
7. Splicing Assessment
8. Regulatory & Expression
9. Structural & Protein Function
10. Computational & AI
11. Clinical Evidence & Curation
12. ACMG/AMP Classification
13. Reporting & Reinterpretation

## Evidence types

- Technical
- Reference/annotation
- Population
- Phenotypic
- Phenotypic/computational
- Clinical/curated
- Computational
- Computational/transcript-based
- Computational/AI
- Regulatory/functional
- Structural/functional
- Clinical/literature
- Integrated clinical evidence
- Clinical/reporting

Phenotypic/computational, transcript-based, and AI-assisted outputs are computational inferences. They are distinguished so that phenotype–gene matching, a splice score, and a curated assertion are not stored as the same kind of evidence. Table 1 assigns Phenotypic/computational to the Phenotype & Gene Prioritization row, including phenotype encoding with HPO. `Phenotypic` remains available when an entry needs to record curated phenotype encoding separately from computational inference.

## Genome-build tokens

Use only these tokens, in this order when more than one applies:

1. `GRCh37`
2. `GRCh38`
3. `build independent`
4. `protein or transcript mapping`
5. `build dependent`

Put release-specific or partial-support detail in `technical_compatibility`.

## Maintenance status

- Active
- Active/verify current status
- Active/legacy use
- Active/subscription
- Active/subscription tiered
- Active/archival
- Context dependent

`Active/subscription tiered` means a usable subset is public and fuller access depends on a paid or registered tier. `Active/archival` means the dataset or site is retained for reference and is no longer the current population or annotation release.

## Curation rules

- Preserve the distinction between observed, curated, or experimental evidence and computational inference.
- Assign a workflow stage only when the resource addresses that stage's analytical question.
- Record genome-build and transcript compatibility wherever they can affect outputs.
- Resources are representative as opposed to mandatory.
- Do not present resource outputs as autonomous clinical categorizations.
- Record known overlap or dependence in `data/resource_dependencies.csv` when relevant.
- Use `candidate` for an entry awaiting appraisal and `retired` for an entry retained only for historical traceability.
- Keep `complementary_resources` inside the catalog. Put laboratory procedures, RNA studies, and other non-catalogued context in `complementary_context`.

## Machine-readable schema

`schemas/resource_catalog.schema.json` is the JSON Schema for `data/resource_catalog.json`.
