# Governance and update policy

## Inclusion criteria

A resource may be entered into the core catalog when it:

1. Serves a defined role in one or more post-analytical stages of germline clinical WES/WGS interpretation.
2. Has sufficient primary documentation, official documentation, or both to identify intended use and output.
3. Has identifiable access, maintenance, version, release, or update information.
4. Has sufficient technical or clinical detail to record inputs, outputs, evidence type, and principal limitations.

Resources with unclear maintenance, inadequate documentation, or no defined interpretive role should not be placed in the core catalog. They may be recorded as `candidate` entries while appraisal is incomplete.

## Update procedure

For each new release or substantive change:

1. Verify the official resource location and maintenance status.
2. Update version/release and access date.
3. Reassess genome-build/transcript compatibility, inputs, outputs, and limitations.
4. Check whether validation evidence, scope, data provenance, or dependencies changed.
5. Document the change in `CHANGELOG.md`.
6. Increment the repository release version using semantic versioning.

## Versioning

- **MAJOR:** schema or workflow changes that affect interpretation of existing entries.
- **MINOR:** addition of resources or substantive updates to multiple entries.
- **PATCH:** corrections, URL updates, wording clarifications, or metadata refreshes.

## Retirement

Do not silently delete a retired resource. Retain a record with status `retired`, explain the reason, record the final known release/access date, and identify a possible successor where appropriate.

## Review expectations

Entries should be reviewed by people with expertise appropriate to the resource domain. Clinical use requires local validation, governance, and qualified professional review; WER-KB does not confer clinical validation.
