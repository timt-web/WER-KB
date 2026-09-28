# Resource catalog schema

## Required fields

| Field | Definition | Allowed/expected values |
|---|---|---|
| `resource_id` | Stable machine-readable identifier | lowercase kebab-case |
| `resource_name` | Public resource name | text |
| `resource_class` | Resource category | tool; database; predictor; ontology; guideline; curation resource; reference |
| `analytical_function` | Main role in WER-KB | one or more framework domains |
| `workflow_stages` | Applicable stages | semicolon-separated integers from 1 to 11 |
| `evidence_type` | Nature of output | Technical; Reference/annotation; Population; Phenotypic; Clinical/curated; Computational; Regulatory/functional; Structural/functional; Clinical/literature; Integrated clinical evidence; Clinical/reporting |
| `primary_purpose` | Defined analytical purpose | concise text |
| `input` | Expected input | concise text |
| `output` | Produced information | concise text |
| `genome_build_compatibility` | Genome build context | explicit builds or build independent |
| `technical_compatibility` | Interfaces/formats and technical constraints | concise text |
| `maintenance_status` | Maintenance state | Active; Active/verify current status; Active/legacy use; Active/subscription; Context dependent |
| `selection_rationale` | Why it is included | concise, auditable text |
| `appropriate_use` | Situations in which it may be appropriate | concise text |
| `interpretation_boundary` | Inferences that must not be made from output alone | concise text |
| `key_limitations` | Material limitations and biases | concise text |
| `complementary_resources` | Resources that may provide distinct complementary context | semicolon-separated names |
| `official_url` | Official home page | URL |
| `version_or_release` | Version/release used or verification instruction | text |
| `access_date` | Date entry was checked | ISO 8601 date |
| `status` | Catalog status | core representative resource; candidate; retired; out of scope |

## Curation rules

- Preserve the distinction between observed/curated/experimental evidence and computational inference.
- Record genome build and transcript context wherever they can affect outputs.
- Do not label a tool as “best” or “required for all cases.”
- Do not present predictors, database assertions, or integrated platforms as autonomous clinical classifiers.
- Record known overlap or dependencies in `data/resource_dependencies.csv` when relevant.
- Use `candidate` for an entry awaiting appraisal and `retired` for entries retained only for historical traceability.
