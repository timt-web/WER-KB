# Contribution guide

## Before proposing a resource

Check that it fits the post-analytical germline WES/WGS scope and meets the inclusion criteria in [`docs/governance.md`](governance.md). Read the scientific question for the relevant stage in [`docs/workflow.md`](workflow.md) and assign the resource only to stages whose question it can address.

## Editing the catalog

1. Copy [`templates/resource_entry_template.md`](../templates/resource_entry_template.md) while drafting.
2. Add or update the row in [`data/resource_catalog.csv`](../data/resource_catalog.csv). Use the controlled values in [`schemas/resource_catalog_schema.md`](../schemas/resource_catalog_schema.md).
3. Put other catalogued resources in `complementary_resources` as `resource_id` values. Put laboratory procedures, RNA studies, and similar context in `complementary_context`.
4. Record the release that was checked in `version_or_release`. Use `not recorded` only when this review did not capture a release, and set `reverify_at_use` to `yes`.
5. If the stage's scientific question or interpretation boundary changes, edit those columns in [`data/workflow_mapping.csv`](../data/workflow_mapping.csv). Leave `representative_resources` to the generator.
6. If the resource shares data, training features, annotations, or primary literature with another entry, update [`data/resource_dependencies.csv`](../data/resource_dependencies.csv).
7. Regenerate the public files and validate:

```bash
python3 scripts/build_catalog.py
python3 scripts/validate_catalog.py
```

8. Describe the change in [`CHANGELOG.md`](../CHANGELOG.md).

Keep the CSV files as the copy you edit. The JSON catalog, the rationale notes, and [`docs/workflow.md`](workflow.md) should match those tables. If you change only those three files, the next run of the commands above will put the table text back, and the check will fail until they match.

## Style rules

- Use neutral language: "included," "may support," "appropriate when," and "should be interpreted alongside."
- Reserve "best," "mandatory," "proves," and "diagnostic" for claims the cited source makes and that remain inside the entry's scope.
- Keep computational prediction distinct from experimental, curated, clinical, and population evidence.
- Preserve traceability by recording the source version and the access date.
