"""Shared catalog vocabulary, loading, and rendering for WER-KB."""

import csv
import json
from datetime import datetime
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COLUMNS = [
    "resource_id",
    "resource_name",
    "resource_class",
    "analytical_function",
    "workflow_stages",
    "evidence_type",
    "primary_purpose",
    "input",
    "output",
    "genome_build_compatibility",
    "technical_compatibility",
    "maintenance_status",
    "selection_rationale",
    "appropriate_use",
    "interpretation_boundary",
    "key_limitations",
    "complementary_resources",
    "complementary_context",
    "official_url",
    "supporting_citation",
    "version_or_release",
    "reverify_at_use",
    "access_date",
    "status",
]

WORKFLOW_COLUMNS = [
    "stage",
    "stage_name",
    "scientific_question",
    "interpretive_boundary",
    "representative_resources",
]

DEPENDENCY_COLUMNS = [
    "evidence_domain",
    "resources",
    "potential_dependency",
    "interpretive_action",
]

RESOURCE_CLASSES = [
    "tool",
    "database",
    "predictor",
    "ontology",
    "guideline",
    "curation resource",
    "reference",
]

ANALYTICAL_FUNCTIONS = [
    "Variant-Level Quality Control & Filtering",
    "Genome & Transcript Annotation",
    "Population & Frequency",
    "Phenotype & Gene Prioritization",
    "Gene–Disease Association",
    "Computational Variant-Effect Prediction",
    "Splicing Assessment",
    "Regulatory & Expression",
    "Structural & Protein Function",
    "Computational & AI",
    "Clinical Evidence & Curation",
    "ACMG/AMP Classification",
    "Reporting & Reinterpretation",
]

LISTED_STATUSES = (
    "core representative resource",
    "candidate",
)

EVIDENCE_TYPES = [
    "Technical",
    "Reference/annotation",
    "Population",
    "Phenotypic",
    "Phenotypic/computational",
    "Clinical/curated",
    "Computational",
    "Computational/transcript-based",
    "Computational/AI",
    "Regulatory/functional",
    "Structural/functional",
    "Clinical/literature",
    "Integrated clinical evidence",
    "Clinical/reporting",
]

BUILD_TOKENS = [
    "GRCh37",
    "GRCh38",
    "build independent",
    "protein or transcript mapping",
    "build dependent",
]

MAINTENANCE_STATUSES = [
    "Active",
    "Active/verify current status",
    "Active/legacy use",
    "Active/subscription",
    "Active/subscription tiered",
    "Active/archival",
    "Context dependent",
]

CATALOG_STATUSES = [
    "core representative resource",
    "candidate",
    "retired",
    "out of scope",
]

PLACEHOLDER_VERSION = "to be confirmed at use"
UNRECORDED_VERSION = "not recorded"

CATALOG_CSV = ROOT / "data" / "resource_catalog.csv"
CATALOG_JSON = ROOT / "data" / "resource_catalog.json"
WORKFLOW_CSV = ROOT / "data" / "workflow_mapping.csv"
DEPENDENCY_CSV = ROOT / "data" / "resource_dependencies.csv"
RATIONALES_MD = ROOT / "docs" / "resource_selection_rationales.md"
WORKFLOW_MD = ROOT / "docs" / "workflow.md"
SCHEMA_JSON = ROOT / "schemas" / "resource_catalog.schema.json"



def split_semi(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = list(reader.fieldnames or [])
        rows = []
        for line_number, row in enumerate(reader, start=2):
            rows.append((line_number, {key: (row.get(key) or "") for key in fieldnames}))
        return fieldnames, rows


def write_csv(path, fieldnames, rows):
    buffer = StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=fieldnames,
        lineterminator="\n",
        extrasaction="ignore",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow({key: row.get(key, "") for key in fieldnames})
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(buffer.getvalue(), encoding="utf-8")


def catalog_rows(root=ROOT):
    _, numbered = read_csv(root / "data" / "resource_catalog.csv")
    return [row for _, row in numbered]


def workflow_rows(root=ROOT):
    _, numbered = read_csv(root / "data" / "workflow_mapping.csv")
    return [row for _, row in numbered]


def dependency_rows(root=ROOT):
    _, numbered = read_csv(root / "data" / "resource_dependencies.csv")
    return [row for _, row in numbered]


def resources_for_stage(rows, stage):
    matched = []
    for row in rows:
        if (row.get("status") or "").strip() not in LISTED_STATUSES:
            continue
        stages = split_semi(row["workflow_stages"])
        if stage in stages:
            matched.append(row["resource_name"])
    return matched


def render_workflow_csv(rows, workflow):
    rendered = []
    for stage_row in workflow:
        updated = dict(stage_row)
        names = resources_for_stage(rows, stage_row["stage"].strip())
        updated["representative_resources"] = "; ".join(names)
        rendered.append(updated)
    buffer = StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=WORKFLOW_COLUMNS,
        lineterminator="\n",
        extrasaction="ignore",
    )
    writer.writeheader()
    for row in rendered:
        writer.writerow({key: row.get(key, "") for key in WORKFLOW_COLUMNS})
    return buffer.getvalue()


def render_json(rows):
    payload = [{column: row[column] for column in COLUMNS} for row in rows]
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def _names_for_ids(rows, id_list):
    by_id = {row["resource_id"]: row["resource_name"] for row in rows}
    return [by_id.get(resource_id, resource_id) for resource_id in id_list]


def _rationale_block(row, rows, heading="##"):
    complements = _names_for_ids(rows, split_semi(row["complementary_resources"]))
    complement_text = "; ".join(complements) if complements else "None listed in the catalog."
    parts = [
        f"{heading} {row['resource_name']}",
        "",
        f"- **Identifier:** {row['resource_id']}",
        f"- **Class:** {row['resource_class']}",
        f"- **Analytical function:** {row['analytical_function']}",
        f"- **Workflow position:** {row['workflow_stages']}",
        f"- **Evidence type:** {row['evidence_type']}",
        f"- **Genome-build and transcript compatibility:** {row['genome_build_compatibility']}",
        f"- **Maintenance:** {row['maintenance_status']}",
        f"- **Official resource:** {row['official_url']}",
        "",
        "### Analytical purpose",
        "",
        row["primary_purpose"],
        "",
        "### Selection rationale",
        "",
        row["selection_rationale"],
        "",
        "### Appropriate use",
        "",
        row["appropriate_use"],
        "",
        "### Interpretation boundary",
        "",
        row["interpretation_boundary"],
        "",
        "### Inputs and outputs",
        "",
        f"Input: {row['input']}",
        "",
        f"Output: {row['output']}",
        "",
        "### Key limitations",
        "",
        row["key_limitations"],
        "",
        "### Complementary resources",
        "",
        complement_text,
        "",
    ]
    if row["complementary_context"].strip():
        parts.extend(
            [
                "### Complementary context",
                "",
                row["complementary_context"],
                "",
            ]
        )
    parts.extend(
        [
            "### Supporting citation",
            "",
            row["supporting_citation"],
            "",
        ]
    )
    if row["version_or_release"] == "not recorded":
        version_note = f"No release identifier was captured when this entry was reviewed on {row['access_date']}."
    else:
        version_note = f"Release reviewed on {row['access_date']}: {row['version_or_release']}."
    if row["reverify_at_use"] == "yes":
        recheck_note = "Check the current release again when the resource is used."
    else:
        recheck_note = "The release cited here is fixed."
    parts.extend(
        [
            "### Traceability",
            "",
            f"{version_note} {recheck_note}",
            "",
        ]
    )
    return parts


def render_rationales(rows):
    listed = [row for row in rows if (row.get("status") or "").strip() in LISTED_STATUSES]
    retained = [row for row in rows if (row.get("status") or "").strip() not in LISTED_STATUSES]
    parts = [
        "# Resource selection rationales",
        "",
        "These notes record the analytical purpose of each representative resource, the context in which it may be used, and the key limitations of its output. Resources are representative as opposed to mandatory.",
        "",
    ]
    for row in listed:
        parts.extend(_rationale_block(row, rows))
    if retained:
        parts.extend(
            [
                "## Retired entries",
                "",
                "These entries are retained for traceability. They are not representative resources in the current workflow mapping.",
                "",
            ]
        )
        for row in retained:
            parts.extend(_rationale_block(row, rows, heading="###"))
    return "\n".join(parts).rstrip() + "\n"


def _dependency_notes(stage_names, dependencies):
    notes = []
    present = set(stage_names)
    for row in dependencies:
        cited = [name for name in split_semi(row["resources"]) if name in present]
        if len(cited) >= 2:
            joined = ", ".join(cited)
            notes.append(
                f"**{row['evidence_domain']}** ({joined}). "
                f"{row['potential_dependency']} {row['interpretive_action']}"
            )
    return notes


def render_workflow_md(rows, workflow, dependencies):
    by_name = {row["resource_name"]: row for row in rows}
    parts = [
        "# Post-analytical workflow",
        "",
        "The framework organizes post-analytical interpretation and prioritization of germline single-nucleotide variants and small insertions/deletions identified through clinical WES/WGS. The 11 stages are the operational structure for the 13 analytical functions. For each stage, the analytical question, the key limitations, and the representative resources are recorded.",
        "",
        "Resources are representative as opposed to mandatory. A resource may be selected, revisited, omitted, or replaced according to the variant, the disease mechanism, the phenotype, the inheritance model, and the evidence already available. Evidence type is shown so that a technical metric, a population frequency, a computational score, and a curated assertion stay distinct.",
        "",
        "Where resources may share datasets, annotations, publications, training data, or modelling assumptions, that dependence is noted. Agreement among those resources is not independent evidence.",
        "",
    ]
    for stage_row in workflow:
        stage = stage_row["stage"].strip()
        names = resources_for_stage(rows, stage)
        parts.extend(
            [
                f"## {stage}. {stage_row['stage_name']}",
                "",
                f"**Analytical question.** {stage_row['scientific_question']}",
                "",
                f"**Key limitations.** {stage_row['interpretive_boundary']}",
                "",
                "### Resources",
                "",
            ]
        )
        grouped = {evidence: [] for evidence in EVIDENCE_TYPES}
        for name in names:
            resource = by_name[name]
            grouped[resource["evidence_type"]].append(resource)
        for evidence in EVIDENCE_TYPES:
            group = grouped[evidence]
            if not group:
                continue
            parts.append(f"#### {evidence}")
            parts.append("")
            for resource in group:
                parts.append(
                    f"- **{resource['resource_name']}** (`{resource['resource_id']}`). "
                    f"{resource['interpretation_boundary']}"
                )
            parts.append("")
        notes = _dependency_notes(names, dependencies)
        if notes:
            parts.append("### Shared sources")
            parts.append("")
            for note in notes:
                parts.append(f"- {note}")
            parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def valid_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def schema_enum_mismatches():
    """Return human-readable differences between the JSON Schema and these constants."""
    if not SCHEMA_JSON.exists():
        return ["JSON Schema file is missing."]
    schema = json.loads(SCHEMA_JSON.read_text(encoding="utf-8"))
    properties = schema["items"]["properties"]
    expected = {
        "resource_class": RESOURCE_CLASSES,
        "evidence_type": EVIDENCE_TYPES,
        "maintenance_status": MAINTENANCE_STATUSES,
        "status": CATALOG_STATUSES,
        "reverify_at_use": ["yes", "no"],
    }
    mismatches = []
    for field, values in expected.items():
        recorded = properties[field].get("enum")
        if recorded != values:
            mismatches.append(f"JSON Schema enum for {field} does not match catalog_lib.")
    required = schema["items"]["required"]
    if required != COLUMNS:
        mismatches.append("JSON Schema required fields do not match catalog columns.")
    return mismatches
