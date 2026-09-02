# Codestra Documentation

Cross-repository architecture, operational documentation, integration-review, and governance authority for the Codestra platform.

## Repository identity

```text
STABLE_GITHUB_REPOSITORY_ID=1350724356
CURRENT_OPERATIONAL_REPOSITORY=appolon1908-hue/documentaions
APPROVED_TARGET_AFTER_CONTROLLED_RENAME=appolon1908-hue/Codestra-Documentation
RENAME_STATUS=PREPARED_NOT_RENAMED
```

The current GitHub slug remains authoritative until the controlled rename procedure is executed and read back. Do not change clone URLs, workflow references, deploy keys, packages, or server remotes to the target name before cutover.

See:

- [`repository-name-migration.v1.json`](repository-name-migration.v1.json) — stable repository IDs, current and target names, migration state, and the PostgreSQL Exporter hostname decision;
- [`REPOSITORY_NAME_MIGRATION_2026-09-02.md`](REPOSITORY_NAME_MIGRATION_2026-09-02.md) — inventory, freeze, rename, validation, rollback, and compatibility-retirement procedure.

Production and runtime changes remain owned by their respective principal service repositories. Documentation in this repository must reference those authorities and must never be treated as deployment, secret rotation, provider activation, financial action, or production-write authorization.

Dated evidence retains the repository names valid when it was captured. Do not rewrite historical source locks, pull-request evidence, release manifests, checksums, or certification reports merely to reflect a later repository rename.