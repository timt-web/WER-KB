# Contribution guide

## Before proposing a resource

Check that it fits the post-analytical germline WES/WGS scope and meets the inclusion criteria in `docs/governance.md`.

## Proposed contribution workflow

1. Copy `templates/resource_entry_template.md`.
2. Complete all required schema fields.
3. Provide official documentation and a release/version or access date.
4. State a concise selection rationale and interpretation boundary.
5. Identify material limitations and likely dependencies.
6. Add the entry to `data/resource_catalog.csv` and `data/resource_catalog.json`.
7. Add a readable rationale entry to `docs/resource_selection_rationales.md`.
8. Update `CHANGELOG.md`.

## Style rules

- Use neutral language: “included,” “may support,” “appropriate when,” and “should be interpreted alongside.”
- Avoid “best,” “mandatory,” “proves,” or “diagnostic” unless such a claim is explicitly supported and within scope.
- Distinguish computational prediction from experimental, curated, clinical, and population evidence.
- Preserve traceability by recording source version and access date.
