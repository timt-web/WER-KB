---
name: Resource addition or update
about: Propose a new resource or update an existing WER-KB entry
---

## Resource name and proposed resource_id

## Proposed change

## Official URL, version or release, and whether it must be rechecked at use

## Workflow stage(s) and analytical function

State the stage question the resource addresses. See `docs/workflow.md`.

## Evidence type and interpretation boundary

## Selection rationale

## Limitations, complementary resource ids, and dependencies

## Supporting documentation

Accepted entries are added to `data/resource_catalog.csv`. Stage questions and dependence notes are updated in the workflow and dependency tables. Then run `python3 scripts/build_catalog.py` so the JSON catalog, the rationale notes, and `docs/workflow.md` match.
