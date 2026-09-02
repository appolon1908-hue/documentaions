# Codestra controlled repository-name migration

**Prepared:** 2026-09-02  
**State:** `PREPARED_NOT_RENAMED`  
**Machine-readable authority:** [`repository-name-migration.v1.json`](repository-name-migration.v1.json)

## Decision

Six GitHub repository names contain spelling errors or unclear legacy naming. They will be corrected through a controlled, one-repository-at-a-time migration. This document does **not** rename a repository, change a deployment, rebuild an image, rotate a secret, update DNS, restart a service, or authorize production traffic.

The stable identity of each repository is its GitHub repository ID. Slugs are mutable labels and must never be the only key in an authority or deployment registry.

| Stable repository ID | Current operational repository | Approved target after cutover | State |
|---:|---|---|---|
| `1221155447` | `appolon1908-hue/Frontend-Resturant-` | `appolon1908-hue/restaurant-frontend` | Prepared, not renamed |
| `1343761049` | `appolon1908-hue/transportaion-Frontend` | `appolon1908-hue/freight-platform-frontend` | Prepared, not renamed |
| `1343962199` | `appolon1908-hue/LARIM-A-Fornt-end` | `appolon1908-hue/LARIM-A-Frontend` | Prepared, not renamed |
| `1351353723` | `appolon1908-hue/Codesrea-Social-` | `appolon1908-hue/Codestra-Social-Control-Plane` | Prepared, not renamed |
| `1350724356` | `appolon1908-hue/documentaions` | `appolon1908-hue/Codestra-Documentation` | Prepared, not renamed |
| `1350724865` | `appolon1908-hue/Infustruction-repo` | `appolon1908-hue/Codestra-Infrastructure` | Prepared, not renamed |

Until the GitHub rename step is explicitly executed and read back, every clone, workflow, deployment, package, source lock, and API operation must continue to use the current operational repository name. Future target names must not be treated as existing repositories before cutover.

## PostgreSQL Exporter hostname decision

The principal source is `appolon1908-hue/Codestra-Postgres-Exporter`.

```text
PUBLIC_HOSTNAME=NONE
PRIVATE_SERVICE_IDENTITY=postgres-exporter:9187
EXPOSURE=PRIVATE_INTERNAL_ONLY
FORBIDDEN_PUBLIC_HOSTNAME=pgex.codestra.media
```

A DNS record or historical reference does not grant public exposure. Prometheus on an approved private monitoring network is the routine consumer. Caddy and Kong must not publish the exporter port.

## Historical-evidence rule

Do not rewrite dated evidence to make history look as though the new slug existed earlier. The following remain immutable records of the names that were in use when the evidence was captured:

- dated source-lock and rollback manifests;
- release manifests tied to an exact Git commit;
- pull-request and workflow evidence;
- repository-review CSV files;
- deployment and certification reports;
- signed checksums and attestations;
- historical incident and migration records.

New documents may annotate a historical reference with the stable repository ID and the current target, but the original evidence is not altered.

## Phase 0 — inventory and freeze packet

Before each individual rename, capture:

```text
repository ID
current full name
current default branch
current default-branch SHA
tag and release inventory
open pull requests and their head/base refs
branch protection and rulesets
GitHub Environment names and protection rules
Actions workflow inventory
repository variables and secret NAMES only
webhook inventory without secret values
deploy-key fingerprints and access level
GitHub App installations
Pages configuration
container/package names
Dependabot and code-scanning configuration
CODEOWNERS and required checks
server and developer Git remotes
Compose, Kubernetes, Terraform, Ansible, and source-lock references
badges, submodules, reusable workflows, and action references
```

Do not print or commit secret values. Record only identifiers, fingerprints, names, paths, and non-secret configuration.

Create an exact pre-change tag or signed evidence record containing the protected default-branch SHA. For runtime-critical repositories, also record the currently deployed image digest and rollback digest before any rename.

## Phase 1 — alias compatibility

Before changing the GitHub slug:

1. Add the stable repository ID, current name, approved target name, and migration state to machine-readable consumers.
2. Make validators accept only the current operational name while `status=PREPARED_NOT_RENAMED`.
3. Make validators require the target name only after an explicitly reviewed state transition.
4. Prevent a missing target repository from being treated as source loss before cutover.
5. Keep historical evidence exempt from replacement while still requiring new authority records to use the migration manifest.
6. Ensure deployment automation fails closed when repository identity cannot be reconciled to the stable ID.

Compatibility means recognition of the planned target; it does not mean silently following any repository with a matching name.

## Phase 2 — change freeze

For the selected repository only:

- stop new merges and release dispatches;
- wait for in-progress workflows to complete or cancel them safely;
- record all open PR heads and bases;
- ensure the default branch is clean and protected;
- verify there is no active deployment reading a mutable branch name without an exact SHA/digest;
- take the repository and runtime rollback snapshots required by its authority class.

Other repositories remain operational and are not renamed in the same change window.

## Phase 3 — GitHub repository rename

The rename is an explicit owner/admin operation. It must use the exact current repository ID and the approved target slug from the manifest.

Immediately read back:

```text
repository ID unchanged
new full name exact
visibility unchanged
default branch unchanged
default-branch SHA unchanged
branch protection/rulesets present
issues and pull requests present
releases and tags present
Actions workflows present
Environments present
packages and attestations accounted for
old web URL redirect behavior recorded
old Git remote behavior recorded
```

If the repository ID changes, source history is missing, protection is absent, or the default SHA differs unexpectedly, stop and roll back before updating consumers.

## Phase 4 — update mutable references

Update only mutable current-state material:

- active authority registries;
- current architecture and service catalogs;
- reusable workflow `uses:` references;
- CI checkout repository values;
- badges and current README links;
- Git submodules;
- package publication configuration;
- GHCR/build labels and current image-source metadata;
- infrastructure module sources;
- deployment scripts and current source locks;
- server and developer Git remotes;
- webhook and GitHub App repository selection where required.

Use the stable repository ID to prove that the old and new full names describe the same repository.

Do not modify immutable dated evidence. Add a superseding current-state manifest instead.

## Phase 5 — Actions, packages, and deployment validation

Require all of the following for the renamed repository:

```text
clone through new URL=PASS
fetch/pull through new URL=PASS
push to protected test branch=PASS
pull-request CI=PASS
merge-result CI=PASS
reusable workflows resolve=PASS
required checks resolve=PASS
CODEOWNERS/reviewer rules=PASS
release workflow dry run=PASS
container/package publication dry run or bounded test=PASS
SBOM/provenance source URL uses current authority=PASS
deployment preflight uses exact repository ID/SHA=PASS
```

A redirect from the old URL is compatibility evidence, not authority for new automation. New automation must use the new full name after cutover.

## Phase 6 — server and runtime readback

For every server checkout and deployment consumer:

1. record the old remote and exact current SHA;
2. change only the remote URL;
3. fetch without merging;
4. prove the repository ID and exact commit still match;
5. prove dirty worktrees were not overwritten;
6. run source-to-runtime and image-label checks;
7. do not restart or redeploy unless separately approved;
8. verify production remains on the same immutable image digest.

A repository rename alone must produce:

```text
WORKLOADS_RESTARTED=0
IMAGES_REBUILT=0
DATABASE_MIGRATIONS=0
PRODUCTION_TRAFFIC_CHANGED=NO
BUSINESS_WRITES_ENABLED=NO_CHANGE
```

## Phase 7 — rollback

Rollback triggers include:

- repository ID mismatch;
- lost or weakened branch protection;
- broken required checks;
- unresolved reusable workflow or submodule;
- package publication loss;
- deployment checkout unable to resolve the protected SHA;
- broken GitHub App, webhook, or deploy-key access;
- source/provenance labels no longer reconcilable;
- any unexpected production change.

Rollback consists of renaming the repository back to its prior slug when safe, restoring mutable references from the pre-change packet, restoring the previous remote URLs, and rerunning the same readback matrix. Do not roll back application databases or runtime images for a metadata-only rename unless a separately deployed change also occurred.

## Phase 8 — compatibility retirement

Keep compatibility references for a defined observation period. Retire an old slug from active validators only after:

- all current repositories and workflows use the new full name;
- every server remote is updated;
- packages, provenance, badges, webhooks, and apps are reconciled;
- no active PR or release process depends on the old name;
- the old URL redirect has been documented;
- rollback evidence is complete.

Historical evidence continues to retain the name valid at its capture date.

## Required cutover result

For each repository return:

```text
REPOSITORY_ID=
OLD_FULL_NAME=
NEW_FULL_NAME=
PRECHANGE_DEFAULT_SHA=
POSTCHANGE_DEFAULT_SHA=
REPOSITORY_ID_UNCHANGED=PASS|FAIL
VISIBILITY_UNCHANGED=PASS|FAIL
PROTECTION_UNCHANGED=PASS|FAIL
ACTIONS_RESOLUTION=PASS|FAIL
PACKAGE_RESOLUTION=PASS|FAIL|N/A
SERVER_REMOTES_UPDATED=<n>/<total>
OLD_URL_COMPATIBILITY=PASS|FAIL|NOT_SUPPORTED
NEW_URL_AUTHORITY=PASS|FAIL
RUNTIME_DIGEST_UNCHANGED=PASS|FAIL|N/A
ROLLBACK_REHEARSAL=PASS|FAIL
PRODUCTION_CHANGED=NO
FINAL_STATUS=PASS|ROLLED_BACK|BLOCKED
```

Do not report a repository as renamed until GitHub readback proves the same stable repository ID at the approved new full name.