#!/usr/bin/env python3
"""Validate the account-wide controlled repository-name migration authority."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "repository-name-migration.v1.json"
RUNBOOK = ROOT / "REPOSITORY_NAME_MIGRATION_2026-09-02.md"
README = ROOT / "README.md"
EXPECTED = {
    1221155447: (
        "appolon1908-hue/Frontend-Resturant-",
        "appolon1908-hue/restaurant-frontend",
        True,
    ),
    1343761049: (
        "appolon1908-hue/transportaion-Frontend",
        "appolon1908-hue/freight-platform-frontend",
        True,
    ),
    1343962199: (
        "appolon1908-hue/LARIM-A-Fornt-end",
        "appolon1908-hue/LARIM-A-Frontend",
        True,
    ),
    1351353723: (
        "appolon1908-hue/Codesrea-Social-",
        "appolon1908-hue/Codestra-Social-Control-Plane",
        False,
    ),
    1350724356: (
        "appolon1908-hue/documentaions",
        "appolon1908-hue/Codestra-Documentation",
        False,
    ),
    1350724865: (
        "appolon1908-hue/Infustruction-repo",
        "appolon1908-hue/Codestra-Infrastructure",
        True,
    ),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load() -> dict[str, Any]:
    try:
        value = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid migration authority JSON: {exc}")
    if not isinstance(value, dict):
        fail("migration authority root must be an object")
    return value


def validate() -> None:
    document = load()
    if document.get("schema_version") != "1.0":
        fail("schema_version must be 1.0")
    if document.get("status") != "PREPARED_NOT_RENAMED":
        fail("account migration status changed without a reviewed cutover")

    authority = document.get("authority")
    if not isinstance(authority, dict):
        fail("documentation authority is missing")
    if authority.get("repository_id") != 1350724356:
        fail("documentation stable repository ID is incorrect")
    if authority.get("current_repository") != "appolon1908-hue/documentaions":
        fail("documentation current repository is incorrect")
    if authority.get("target_repository_after_cutover") != (
        "appolon1908-hue/Codestra-Documentation"
    ):
        fail("documentation target repository is incorrect")

    rules = document.get("rules")
    if not isinstance(rules, dict):
        fail("migration rules are missing")
    required_true = {
        "current_slug_remains_operational_until_cutover",
        "target_slug_must_not_be_used_for_clone_or_automation_before_cutover",
        "historical_evidence_is_immutable",
        "dated_source_locks_are_not_rewritten",
        "one_repository_per_cutover",
        "post_cutover_readback_required",
        "all_inventoried_integrations_require_post_rename_readback",
        "runtime_evidence_required_only_when_deployment_exists",
        "absent_runtime_must_be_recorded_as_not_applicable",
        "success_path_must_restore_freeze_state",
        "rollback_path_must_restore_freeze_state",
    }
    for key in required_true:
        if rules.get(key) is not True:
            fail(f"required fail-closed migration rule is not true: {key}")
    for key in {
        "rename_is_not_deployment_authorization",
        "rename_is_not_image_rebuild_authorization",
        "rename_is_not_secret_rotation_authorization",
    }:
        if rules.get(key) is not True:
            fail(f"required non-authorization rule is not true: {key}")
    if rules.get("stable_identity_key") != "repository_id":
        fail("repository_id must be the stable identity key")

    renames = document.get("renames")
    if not isinstance(renames, list) or len(renames) != len(EXPECTED):
        fail("migration authority must contain exactly six repositories")

    actual: dict[int, tuple[str, str, bool]] = {}
    repository_ids: set[int] = set()
    current_names: set[str] = set()
    target_names: set[str] = set()
    for item in renames:
        if not isinstance(item, dict):
            fail("rename entry must be an object")
        repository_id = item.get("repository_id")
        current = item.get("current_repository")
        target = item.get("target_repository_after_cutover")
        runtime_critical = item.get("runtime_critical")
        if not isinstance(repository_id, int) or repository_id <= 0:
            fail("rename entry contains an invalid repository ID")
        if repository_id in repository_ids:
            fail(f"duplicate repository ID: {repository_id}")
        if not isinstance(current, str) or not current.startswith("appolon1908-hue/"):
            fail(f"invalid current repository for ID {repository_id}")
        if not isinstance(target, str) or not target.startswith("appolon1908-hue/"):
            fail(f"invalid target repository for ID {repository_id}")
        if current == target:
            fail(f"current and target names are identical for ID {repository_id}")
        if current in current_names or target in target_names:
            fail("duplicate current or target repository name")
        if item.get("status") != "PREPARED_NOT_RENAMED":
            fail(f"rename state changed without cutover: {current}")
        if not isinstance(runtime_critical, bool):
            fail(f"runtime_critical must be boolean for ID {repository_id}")
        actual[repository_id] = (current, target, runtime_critical)
        repository_ids.add(repository_id)
        current_names.add(current)
        target_names.add(target)

    if actual != EXPECTED:
        fail("repository IDs, current names, targets, or criticality do not match authority")

    exporter = document.get("postgres_exporter_authority")
    if not isinstance(exporter, dict):
        fail("PostgreSQL Exporter authority is missing")
    if exporter.get("repository_id") != 1350839865:
        fail("PostgreSQL Exporter stable ID is incorrect")
    if exporter.get("repository") != "appolon1908-hue/Codestra-Postgres-Exporter":
        fail("PostgreSQL Exporter principal repository is incorrect")
    if exporter.get("public_hostname") is not None:
        fail("PostgreSQL Exporter may not have a public hostname")
    if exporter.get("private_service_identity") != "postgres-exporter:9187":
        fail("PostgreSQL Exporter private service identity is incorrect")
    if exporter.get("forbidden_public_hostname") != "pgex.codestra.media":
        fail("retired PostgreSQL Exporter hostname is not explicitly forbidden")
    if exporter.get("exposure") != "PRIVATE_INTERNAL_ONLY":
        fail("PostgreSQL Exporter exposure must remain private/internal")
    for field in (
        "caddy_publication_allowed",
        "kong_publication_allowed",
        "host_public_port_allowed",
    ):
        if exporter.get(field) is not False:
            fail(f"PostgreSQL Exporter {field} must remain false")

    phases = document.get("cutover_phases")
    required_phases = [
        "inventory",
        "alias_compatibility",
        "change_freeze",
        "github_repository_rename",
        "post_rename_integration_readback",
        "mutable_reference_update",
        "actions_and_package_validation",
        "server_remote_readback",
        "rollback_rehearsal",
        "operations_unfreeze",
        "compatibility_retirement",
    ]
    if phases != required_phases:
        fail("controlled cutover phases are incomplete or reordered")

    runbook = RUNBOOK.read_text(encoding="utf-8")
    for required in (
        "PREPARED_NOT_RENAMED",
        "Historical-evidence rule",
        "post-rename integration readback",
        "server and runtime readback",
        "rollback rehearsal",
        "operations unfreeze",
        "CURRENT_RUNTIME_STATE=DEPLOYED|NOT_DEPLOYED",
        "DEPLOYED_IMAGE_DIGEST=<immutable-digest>|N/A",
        "RUNTIME_DIGEST_UNCHANGED=PASS|FAIL|N/A",
        "MERGES_UNFROZEN=PASS|FAIL",
        "WORKFLOW_DISPATCH_UNFROZEN=PASS|FAIL|N/A",
        "ROLLBACK_UNFREEZE=PASS|FAIL|N/A",
        "WORKLOADS_RESTARTED=0",
        "PRODUCTION_CHANGED=NO",
    ):
        if required.lower() not in runbook.lower():
            fail(f"migration runbook is missing required evidence: {required}")

    readme = README.read_text(encoding="utf-8")
    for required in (
        "STABLE_GITHUB_REPOSITORY_ID=1350724356",
        "CURRENT_OPERATIONAL_REPOSITORY=appolon1908-hue/documentaions",
        "APPROVED_TARGET_AFTER_CONTROLLED_RENAME=appolon1908-hue/Codestra-Documentation",
        "RENAME_STATUS=PREPARED_NOT_RENAMED",
    ):
        if required not in readme:
            fail(f"README is missing documentation repository identity: {required}")


def main() -> None:
    validate()
    print("Codestra account-wide repository-name migration authority: PASS")


if __name__ == "__main__":
    main()
