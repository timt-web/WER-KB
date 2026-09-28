#!/usr/bin/env python3
import csv
from pathlib import Path

required = {"resource_id", "resource_name", "resource_class", "analytical_function", "workflow_stages", "evidence_type", "primary_purpose", "selection_rationale", "appropriate_use", "interpretation_boundary", "key_limitations", "official_url", "version_or_release", "access_date", "status"}
path = Path(__file__).resolve().parents[1] / "data" / "resource_catalog.csv"
with path.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    missing = required - set(reader.fieldnames or [])
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    seen = set()
    count = 0
    for row in reader:
        count += 1
        if not row["resource_id"] or row["resource_id"] in seen:
            raise SystemExit(f"Invalid or duplicate resource_id: {row.get('resource_id')!r}")
        seen.add(row["resource_id"])
        stages = [s.strip() for s in row["workflow_stages"].split(";") if s.strip()]
        if not stages or any(not s.isdigit() or not 1 <= int(s) <= 11 for s in stages):
            raise SystemExit(f"Invalid workflow stages for {row['resource_name']}: {row['workflow_stages']}")
print(f"Validated {count} resource entries.")
