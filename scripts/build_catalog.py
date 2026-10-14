#!/usr/bin/env python3
"""Regenerate JSON, rationales, the workflow page, and stage resource lists."""

import sys
from pathlib import Path

from catalog_lib import (
    catalog_rows,
    dependency_rows,
    render_json,
    render_rationales,
    render_workflow_csv,
    render_workflow_md,
    workflow_rows,
)


def build(root=None):
    root = Path(root) if root else Path(__file__).resolve().parents[1]
    rows = catalog_rows(root)
    workflow = workflow_rows(root)
    dependencies = dependency_rows(root)

    outputs = {
        root / "data" / "resource_catalog.json": render_json(rows),
        root / "docs" / "resource_selection_rationales.md": render_rationales(rows),
        root / "docs" / "workflow.md": render_workflow_md(rows, workflow, dependencies),
        root / "data" / "workflow_mapping.csv": render_workflow_csv(rows, workflow),
    }
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return outputs


def main():
    outputs = build()
    for path in outputs:
        print(f"Wrote {path.relative_to(Path(__file__).resolve().parents[1])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
