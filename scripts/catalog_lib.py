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
    "Variant-level quality control and filtering",
    "Genome and transcript annotation",
    "Population-frequency assessment",
    "Phenotype encoding and phenotype-driven gene prioritization",
    "Gene–disease association assessment",
    "Computational variant-effect prediction",
    "Splicing assessment",
    "Regulatory and expression evidence",
    "Structural and protein-function evidence",
    "Computational and AI-assisted prioritization",
    "Clinical evidence retrieval and curation",
    "ACMG/AMP-based variant classification",
    "Reporting, documentation, and reinterpretation",
]

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


def render_rationales(rows):
    parts = [
        "# Resource selection rationales",
        "",
        "These notes record why a resource is in the catalog, the situation in which it can be useful, and the limit of what its output can support. Presence in the catalog does not mean the resource should be used in every case.",
        "",
    ]
    for row in rows:
        complements = _names_for_ids(rows, split_semi(row["complementary_resources"]))
        complement_text = "; ".join(complements) if complements else "None listed in the catalog."
        parts.extend(
            [
                f"## {row['resource_name']}",
                "",
                f"- **Identifier:** {row['resource_id']}",
                f"- **Class:** {row['resource_class']}",
                f"- **Analytical function:** {row['analytical_function']}",
                f"- **Workflow stage(s):** {row['workflow_stages']}",
                f"- **Evidence type:** {row['evidence_type']}",
                f"- **Genome build:** {row['genome_build_compatibility']}",
                f"- **Maintenance:** {row['maintenance_status']}",
                f"- **Official resource:** {row['official_url']}",
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
        )
        if row["complementary_context"].strip():
            parts.extend(
                [
                    "### Complementary context",
                    "",
                    row["complementary_context"],
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
        "Once a germline single-nucleotide variant or small indel has been called from a clinical exome or genome, the catalog follows the work in 11 stages. For each stage we give the question, the limit of what that result can decide, and the resources that address the question.",
        "",
        "Listing a resource under a stage means it is a reasonable option for that question. It does not mean every laboratory must run it. Evidence type is shown so that a quality metric, an allele count, a prediction score, and a curated assertion stay distinct.",
        "",
        "If two resources in the same stage can share assays, training data, annotations, or papers, that overlap is noted there. Concordant results from those resources are not independent evidence.",
        "",
    ]
    for stage_row in workflow:
        stage = stage_row["stage"].strip()
        names = resources_for_stage(rows, stage)
        parts.extend(
            [
                f"## {stage}. {stage_row['stage_name']}",
                "",
                f"**Question.** {stage_row['scientific_question']}",
                "",
                f"**Limit.** {stage_row['interpretive_boundary']}",
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
