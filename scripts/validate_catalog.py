#!/usr/bin/env python3
"""Validate the WER-KB catalog, workflow, dependencies, and generated files."""

import re
import sys
from pathlib import Path

from catalog_lib import (
    ANALYTICAL_FUNCTIONS,
    BUILD_TOKENS,
    CATALOG_STATUSES,
    COLUMNS,
    DEPENDENCY_COLUMNS,
    EVIDENCE_TYPES,
    MAINTENANCE_STATUSES,
    PLACEHOLDER_VERSION,
    RESOURCE_CLASSES,
    UNRECORDED_VERSION,
    WORKFLOW_COLUMNS,
    read_csv,
    render_json,
    render_rationales,
    render_workflow_csv,
    render_workflow_md,
    resources_for_stage,
    schema_enum_mismatches,
    split_semi,
    valid_date,
)

ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_PATTERN = re.compile(r"^https?://\S+$")

REQUIRED_NONEMPTY = [column for column in COLUMNS if column != "complementary_context"]


def _stage_numbers(value):
    numbers = []
    for token in split_semi(value):
        if not token.isdigit():
            return None
        numbers.append(int(token))
    return numbers


def row_errors(line_number, row, known_ids):
    errors = []
    prefix = f"{row.get('resource_id') or 'row ' + str(line_number)} (line {line_number})"

    for column in REQUIRED_NONEMPTY:
        if not (row.get(column) or "").strip():
            errors.append(f"{prefix}: empty {column}")

    resource_id = (row.get("resource_id") or "").strip()
    if resource_id and not ID_PATTERN.fullmatch(resource_id):
        errors.append(f"{prefix}: resource_id must be lowercase kebab-case")

    resource_class = (row.get("resource_class") or "").strip()
    if resource_class and resource_class not in RESOURCE_CLASSES:
        errors.append(f"{prefix}: unknown resource_class {resource_class!r}")

    functions = split_semi(row.get("analytical_function"))
    if functions:
        unknown = [item for item in functions if item not in ANALYTICAL_FUNCTIONS]
        if unknown:
            errors.append(f"{prefix}: unknown analytical_function {unknown!r}")
        if len(functions) != len(set(functions)):
            errors.append(f"{prefix}: repeated analytical_function")

    stages = _stage_numbers(row.get("workflow_stages"))
    if stages is None or not stages:
        errors.append(f"{prefix}: workflow_stages must be integers from 1 to 11")
    else:
        if any(stage < 1 or stage > 11 for stage in stages):
            errors.append(f"{prefix}: workflow stage outside 1–11")
        if stages != sorted(set(stages)):
            errors.append(f"{prefix}: workflow_stages must be unique and ascending")

    evidence = (row.get("evidence_type") or "").strip()
    if evidence and evidence not in EVIDENCE_TYPES:
        errors.append(f"{prefix}: unknown evidence_type {evidence!r}")

    builds = split_semi(row.get("genome_build_compatibility"))
    if builds:
        unknown = [item for item in builds if item not in BUILD_TOKENS]
        if unknown:
            errors.append(f"{prefix}: unknown genome-build token {unknown!r}")
        expected_order = [token for token in BUILD_TOKENS if token in builds]
        if builds != expected_order or len(builds) != len(set(builds)):
            errors.append(f"{prefix}: genome-build tokens must be unique and in schema order")

    maintenance = (row.get("maintenance_status") or "").strip()
    if maintenance and maintenance not in MAINTENANCE_STATUSES:
        errors.append(f"{prefix}: unknown maintenance_status {maintenance!r}")

    status = (row.get("status") or "").strip()
    if status and status not in CATALOG_STATUSES:
        errors.append(f"{prefix}: unknown status {status!r}")

    url = (row.get("official_url") or "").strip()
    if url and not URL_PATTERN.fullmatch(url):
        errors.append(f"{prefix}: official_url must be an absolute http(s) URL")

    version = (row.get("version_or_release") or "").strip()
    reverify = (row.get("reverify_at_use") or "").strip()
    if version.lower() == PLACEHOLDER_VERSION:
        errors.append(f"{prefix}: version_or_release must name a release or be 'not recorded'")
    if reverify and reverify not in {"yes", "no"}:
        errors.append(f"{prefix}: reverify_at_use must be yes or no")
    if version == UNRECORDED_VERSION and reverify != "yes":
        errors.append(f"{prefix}: not recorded version requires reverify_at_use=yes")

    access_date = (row.get("access_date") or "").strip()
    if access_date and not valid_date(access_date):
        errors.append(f"{prefix}: access_date must be a real YYYY-MM-DD date")

    complements = split_semi(row.get("complementary_resources"))
    if len(complements) != len(set(complements)):
        errors.append(f"{prefix}: repeated complementary resource")
    for complement in complements:
        if not ID_PATTERN.fullmatch(complement):
            errors.append(f"{prefix}: complementary resource {complement!r} is not a resource_id")
        elif complement == resource_id:
            errors.append(f"{prefix}: complementary resource points at itself")
        elif known_ids and complement not in known_ids:
            errors.append(f"{prefix}: unknown complementary resource {complement!r}")

    return errors


def catalog_errors(numbered_rows):
    errors = []
    ids = []
    names = []
    for _, row in numbered_rows:
        ids.append((row.get("resource_id") or "").strip())
        names.append((row.get("resource_name") or "").strip())
    known_ids = {resource_id for resource_id in ids if resource_id}

    seen_ids = set()
    seen_names = set()
    for line_number, row in numbered_rows:
        resource_id = (row.get("resource_id") or "").strip()
        resource_name = (row.get("resource_name") or "").strip()
        if resource_id and resource_id in seen_ids:
            errors.append(f"{resource_id} (line {line_number}): duplicate resource_id")
        seen_ids.add(resource_id)
        if resource_name and resource_name in seen_names:
            errors.append(f"{resource_id} (line {line_number}): duplicate resource_name")
        seen_names.add(resource_name)
        errors.extend(row_errors(line_number, row, known_ids))
    return errors


def workflow_errors(workflow_numbered, rows):
    errors = []
    by_name = {row["resource_name"]: row for row in rows}
    seen_stages = []
    for line_number, stage_row in workflow_numbered:
        stage = (stage_row.get("stage") or "").strip()
        label = f"workflow stage {stage or line_number} (line {line_number})"
        if stage not in {str(number) for number in range(1, 12)}:
            errors.append(f"{label}: stage must be an integer from 1 to 11")
        elif stage in seen_stages:
            errors.append(f"{label}: duplicate stage")
        else:
            seen_stages.append(stage)
        for column in ("stage_name", "scientific_question", "interpretive_boundary"):
            if not (stage_row.get(column) or "").strip():
                errors.append(f"{label}: empty {column}")
        if not stage.isdigit():
            continue
        expected = resources_for_stage(rows, stage)
        recorded = split_semi(stage_row.get("representative_resources"))
        if recorded != expected:
            errors.append(
                f"{label}: representative_resources must be generated from the catalog "
                f"(expected {'; '.join(expected)!r})"
            )
        for name in recorded:
            resource = by_name.get(name)
            if resource is None:
                errors.append(f"{label}: {name!r} is not a catalog resource_name")
            elif stage not in split_semi(resource["workflow_stages"]):
                errors.append(f"{label}: {name} does not claim this stage in the catalog")

    if seen_stages != [str(number) for number in range(1, 12)]:
        errors.append("workflow map must contain stages 1 through 11 exactly once")

    for row in rows:
        for stage in split_semi(row["workflow_stages"]):
            listed = resources_for_stage(rows, stage)
            if row["resource_name"] not in listed:
                errors.append(
                    f"{row['resource_id']}: claims stage {stage} but is absent from the generated map"
                )
    return errors


def dependency_errors(dependency_numbered, rows):
    errors = []
    names = {row["resource_name"] for row in rows}
    for line_number, row in dependency_numbered:
        domain = (row.get("evidence_domain") or "").strip() or f"line {line_number}"
        for column in DEPENDENCY_COLUMNS:
            if not (row.get(column) or "").strip():
                errors.append(f"dependency {domain}: empty {column}")
        cited = split_semi(row.get("resources"))
        if len(cited) < 2:
            errors.append(f"dependency {domain}: list at least two resources")
        for name in cited:
            if name not in names:
                errors.append(f"dependency {domain}: {name!r} is not a catalog resource_name")
    return errors


def freshness_errors(root, rows, workflow, dependencies):
    expected = {
        Path("data/resource_catalog.json"): render_json(rows),
        Path("docs/resource_selection_rationales.md"): render_rationales(rows),
        Path("docs/workflow.md"): render_workflow_md(rows, workflow, dependencies),
        Path("data/workflow_mapping.csv"): render_workflow_csv(rows, workflow),
    }
    errors = []
    for relative, content in expected.items():
        path = root / relative
        if not path.exists():
            errors.append(f"missing generated file {relative.as_posix()}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != content:
            errors.append(
                f"{relative.as_posix()} is stale; run python3 scripts/build_catalog.py"
            )
    return errors


def collect_errors(root):
    root = Path(root)
    errors = []
    catalog_path = root / "data" / "resource_catalog.csv"
    workflow_path = root / "data" / "workflow_mapping.csv"
    dependency_path = root / "data" / "resource_dependencies.csv"

    if not catalog_path.exists():
        return ["missing data/resource_catalog.csv"]

    catalog_fields, catalog_numbered = read_csv(catalog_path)
    if catalog_fields != COLUMNS:
        errors.append(f"catalog columns must be {COLUMNS}")
    rows = [row for _, row in catalog_numbered]
    errors.extend(catalog_errors(catalog_numbered))

    if workflow_path.exists():
        workflow_fields, workflow_numbered = read_csv(workflow_path)
        if workflow_fields != WORKFLOW_COLUMNS:
            errors.append(f"workflow columns must be {WORKFLOW_COLUMNS}")
        workflow = [row for _, row in workflow_numbered]
        errors.extend(workflow_errors(workflow_numbered, rows))
    else:
        workflow = []
        errors.append("missing data/workflow_mapping.csv")

    if dependency_path.exists():
        dependency_fields, dependency_numbered = read_csv(dependency_path)
        if dependency_fields != DEPENDENCY_COLUMNS:
            errors.append(f"dependency columns must be {DEPENDENCY_COLUMNS}")
        dependencies = [row for _, row in dependency_numbered]
        errors.extend(dependency_errors(dependency_numbered, rows))
    else:
        dependencies = []
        errors.append("missing data/resource_dependencies.csv")

    if not errors:
        errors.extend(freshness_errors(root, rows, workflow, dependencies))
    if root.resolve() == Path(__file__).resolve().parents[1]:
        errors.extend(schema_enum_mismatches())
    return errors


def main(argv=None):
    root = Path(__file__).resolve().parents[1]
    if argv:
        root = Path(argv[0])
    errors = collect_errors(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"{len(errors)} validation error(s).", file=sys.stderr)
        return 1
    _, numbered = read_csv(root / "data" / "resource_catalog.csv")
    print(f"Validated {len(numbered)} resource entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
