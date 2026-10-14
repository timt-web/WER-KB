"""Validator tests for WER-KB."""

import csv
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import catalog_lib  # noqa: E402
import validate_catalog  # noqa: E402


def _minimal_row(**overrides):
    row = {column: "value" for column in catalog_lib.COLUMNS}
    row.update(
        {
            "resource_id": "example-tool",
            "resource_name": "Example tool",
            "resource_class": "tool",
            "analytical_function": "Variant-Level Quality Control & Filtering",
            "workflow_stages": "1",
            "evidence_type": "Technical",
            "genome_build_compatibility": "GRCh38",
            "maintenance_status": "Active",
            "complementary_resources": "",
            "complementary_context": "",
            "official_url": "https://example.org/tool",
            "version_or_release": "not recorded",
            "reverify_at_use": "yes",
            "access_date": "2026-10-10",
            "status": "core representative resource",
        }
    )
    row.update(overrides)
    return row


class RowValidationTests(unittest.TestCase):
    def test_placeholder_version_is_rejected(self):
        row = _minimal_row(version_or_release="To be confirmed at use")
        errors = validate_catalog.row_errors(2, row, {"example-tool"})
        self.assertTrue(any("version_or_release" in error for error in errors))

    def test_unrecorded_version_requires_recheck(self):
        row = _minimal_row(version_or_release="not recorded", reverify_at_use="no")
        errors = validate_catalog.row_errors(2, row, {"example-tool"})
        self.assertTrue(any("reverify_at_use" in error for error in errors))

    def test_unknown_evidence_type_is_rejected(self):
        row = _minimal_row(evidence_type="Phenotypic/computational score")
        errors = validate_catalog.row_errors(2, row, {"example-tool"})
        self.assertTrue(any("evidence_type" in error for error in errors))

    def test_retired_resources_are_omitted_from_stage_lists(self):
        rows = [
            _minimal_row(),
            _minimal_row(
                resource_id="old-tool",
                resource_name="Old tool",
                status="retired",
            ),
        ]
        self.assertEqual(catalog_lib.resources_for_stage(rows, "1"), ["Example tool"])


class FixtureTests(unittest.TestCase):
    def test_duplicate_resource_id_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "data"
            data.mkdir()
            row = _minimal_row()
            with (data / "resource_catalog.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=catalog_lib.COLUMNS, lineterminator="\n")
                writer.writeheader()
                writer.writerow(row)
                writer.writerow(row)
            errors = validate_catalog.collect_errors(root)
            self.assertTrue(any("duplicate resource_id" in error for error in errors))


class RepositoryTests(unittest.TestCase):
    def test_schema_enums_match_validator(self):
        self.assertEqual(catalog_lib.schema_enum_mismatches(), [])

    def test_repository_catalog_validates(self):
        self.assertEqual(validate_catalog.collect_errors(ROOT), [])

    def test_stale_generated_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "data", root / "data")
            shutil.copytree(ROOT / "docs", root / "docs")
            shutil.copytree(ROOT / "schemas", root / "schemas")
            rationale = root / "docs" / "resource_selection_rationales.md"
            rationale.write_text(rationale.read_text(encoding="utf-8") + "\nEdited by hand.\n", encoding="utf-8")
            errors = validate_catalog.collect_errors(root)
            self.assertTrue(any("resource_selection_rationales.md is stale" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
