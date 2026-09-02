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
CADDY_PUBLICATION_ALLOWED=NO
KONG_PUBLICATION_ALLOWED=NO
HOST_PUBLIC_PORT_ALLOWED=NO
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

## Phase 0 — inventory

Before each individual rename, capture a checksum-bound pre-change packet containing:

```text
repository ID
current full name
current visibility
current default branch
current default-branch SHA
tag and release inventory
open pull requests and their head/base refs
branch protection and rulesets
CODEOWNERS and required checks
GitHub Environment names and protection rules
Actions workflow and reusable-workflow inventory
repository variables and secret NAMES only
webhook inventory without secret values
deploy-key fingerprints and access level
GitHub App installations
Pages configuration
container and package names
GHCR identities and provenance source URLs
Dependabot and code-scanning configuration
server and developer Git remotes
Compose, Kubernetes, Terraform, Ansible, and current source-lock references
badges, submodules, workflow uses, and action references
recorded merge, release-dispatch, and workflow-dispatch state
```

Do not print or commit secret values. Record only identifiers, fingerprints, names, paths, and non-secret configuration.

For runtime evidence:

- when a reviewed staging or production deployment exists, record its exact immutable image digest, rollback digest, source revision, and current runtime readback;
- when no deployment exists, record `CURRENT_RUNTIME_STATE=NOT_DEPLOYED`, `DEPLOYED_IMAGE_DIGEST=N/A`, and `RUNTIME_DIGEST_UNCHANGED=N/A`;
- never fabricate an image digest merely because a repository is classified as runtime-critical.

## Phase 1 — alias compatibility

Before changing the GitHub slug:

1. Add the stable repository ID, current name, approved target name, and migration state to machine-readable consumers.
2. Make validators accept only the current operational name while `status=PREPARED_NOT_RENAMED`.
3. Make validators require the target name only after an explicitly reviewed state transition.
4. Prevent a missing target repository from being treated as source loss before cutover.
5. Keep historical evidence exempt from replacement while requiring new current-state authority records to use the migration manifest.
6. Ensure deployment automation fails closed when repository identity cannot be reconciled to the stable ID.
7. Verify no active source lock, workflow, package, deployment, or server remote uses the target slug before cutover.

Compatibility means recognition of the planned target; it does not mean silently following any repository with a matching name.

## Phase 2 — change freeze

For the selected repository only:

- stop new merges, release dispatches, workflow dispatches, and deployment dispatches;
- wait for in-progress workflows to complete or cancel them safely;
- record all open pull-request heads and bases;
- ensure the default branch is clean and protected;
- verify there is no active deployment reading a mutable branch name without an exact SHA and digest;
- take the repository and runtime rollback snapshots required by its authority class;
- record exactly which operations were frozen so they can be restored after success or rollback.

Other repositories remain operational and are not renamed in the same change window.

## Phase 3 — GitHub repository rename

The rename is an explicit owner or administrator operation. It must use the exact current repository ID and approved target slug from the manifest. Creating a second repository with the corrected name is prohibited.

Do not update downstream consumers until Phase 4 passes.

## Phase 4 — post-rename integration readback

Immediately read back every item captured in Phase 0:

```text
repository ID unchanged
new full name exact
visibility unchanged
default branch unchanged
default-branch SHA unchanged
history present
branch protection and rulesets unchanged
CODEOWNERS and required checks present
issues and pull requests present
releases and tags present
Actions workflows present and resolvable
reusable workflows resolve
GitHub Environments present with unchanged protection
packages, GHCR identities, attestations, and provenance accounted for
deploy-key fingerprints and access unchanged
GitHub App installations present
webhook bindings present without secret readback
Pages configuration accounted for
old web URL compatibility recorded
old Git remote behavior recorded
```

If any inventoried integration is missing, weakened, or unresolved, stop before updating consumers and execute rollback.

A redirect from the old URL is compatibility evidence, not new authority. Repository ID and exact protected SHA continuity are the authority proof.

## Phase 5 — update mutable references

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

## Phase 6 — Actions, packages, and deployment validation

Require all applicable checks for the renamed repository:

```text
clone through new URL=PASS
fetch and pull through new URL=PASS
push to protected test branch=PASS
pull-request CI=PASS
merge-result CI=PASS
reusable workflows resolve=PASS
required checks resolve=PASS
CODEOWNERS and reviewer rules=PASS
GitHub Environments and protection=PASS
release workflow dry run=PASS
container or package publication dry run or bounded test=PASS|N/A
SBOM and provenance source URL uses current authority=PASS|N/A
deploy keys=PASS|N/A
GitHub Apps=PASS|N/A
webhooks=PASS|N/A
Pages=PASS|N/A
deployment preflight uses exact repository ID and SHA=PASS
all downstream consumers resolve=PASS
```

New automation must use the new full name only after the rename and same-ID readback pass.

## Phase 7 — server and runtime readback

For every server checkout and deployment consumer:

1. record the old remote and exact current SHA;
2. change only the remote URL;
3. fetch without merging;
4. prove the repository ID and exact commit still match;
5. prove dirty worktrees were not overwritten;
6. run source-to-runtime and image-label checks;
7. do not restart or redeploy unless separately approved;
8. when a deployment exists, verify production or staging remains on the same immutable image digest;
9. when no deployment exists, retain the explicit `N/A` runtime result.

A repository rename alone must produce:

```text
WORKLOADS_RESTARTED=0
IMAGES_REBUILT=0
DATABASE_MIGRATIONS=0
PRODUCTION_TRAFFIC_CHANGED=NO
BUSINESS_WRITES_ENABLED=NO_CHANGE
```

## Phase 8 — rollback rehearsal

Rollback triggers include:

- repository ID mismatch;
- lost or weakened branch protection;
- broken required checks or CODEOWNERS;
- unresolved Actions or reusable workflows;
- missing package, GHCR, attestation, or provenance identity;
- deployment checkout unable to resolve the protected SHA;
- broken GitHub App, webhook, deploy-key, Environment, or Pages binding;
- source/provenance labels no longer reconcilable;
- any unexpected runtime, traffic, provider, database, or business-write change.

Rollback consists of:

1. stopping further mutable-reference changes;
2. renaming the repository back to its prior slug when safe;
3. restoring mutable references and remote URLs from the checksum-bound pre-change packet;
4. rerunning the complete Phase 4, Phase 6, and Phase 7 readback matrix;
5. confirming runtime digests and business capabilities remain unchanged or explicitly `N/A`;
6. restoring the recorded merge, release-dispatch, workflow-dispatch, and deployment-dispatch state only after rollback validation passes.

Do not roll back application databases or runtime images for a metadata-only rename unless a separately deployed change also occurred.

## Phase 9 — operations unfreeze

After the success path or validated rollback:

- restore the exact recorded merge policy;
- restore release-dispatch and workflow-dispatch availability;
- restore deployment-dispatch availability only to its prior approved state;
- prove required checks and branch protection still gate merges;
- record who restored each frozen operation and the readback result.

A successful cutover or rollback must not leave normal repository operations frozen. Unfreeze is not permission to weaken protection or enable a previously disabled deployment.

## Phase 10 — compatibility retirement

Keep compatibility references for a defined observation period. Retire an old slug from active validators only after:

- all current repositories and workflows use the new full name;
- every server and developer remote is updated;
- packages, provenance, badges, webhooks, deploy keys, Apps, Environments, and Pages are reconciled;
- no active pull request or release process depends on the old name;
- the old URL redirect behavior has been documented;
- rollback evidence is complete;
- operations have been unfrozen to the exact pre-change policy.

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
CODEOWNERS_REQUIRED_CHECKS=PASS|FAIL|N/A
ACTIONS_RESOLUTION=PASS|FAIL
REUSABLE_WORKFLOWS=PASS|FAIL|N/A
ENVIRONMENTS=PASS|FAIL|N/A
PACKAGE_GHCR_RESOLUTION=PASS|FAIL|N/A
DEPLOY_KEYS=PASS|FAIL|N/A
GITHUB_APPS=PASS|FAIL|N/A
WEBHOOKS=PASS|FAIL|N/A
PAGES=PASS|FAIL|N/A
DOWNSTREAM_CONSUMERS=PASS|FAIL
SERVER_REMOTES_UPDATED=<n>/<total>
OLD_URL_COMPATIBILITY=PASS|FAIL|NOT_SUPPORTED
NEW_URL_AUTHORITY=PASS|FAIL
CURRENT_RUNTIME_STATE=DEPLOYED|NOT_DEPLOYED
DEPLOYED_IMAGE_DIGEST=<immutable-digest>|N/A
RUNTIME_DIGEST_UNCHANGED=PASS|FAIL|N/A
MERGES_UNFROZEN=PASS|FAIL
RELEASE_DISPATCH_UNFROZEN=PASS|FAIL|N/A
WORKFLOW_DISPATCH_UNFROZEN=PASS|FAIL|N/A
DEPLOYMENT_DISPATCH_RESTORED=PASS|FAIL|N/A
ROLLBACK_REHEARSAL=PASS|FAIL
ROLLBACK_UNFREEZE=PASS|FAIL|N/A
WORKLOADS_RESTARTED=0
IMAGES_REBUILT=0
DATABASE_MIGRATIONS=0
PRODUCTION_CHANGED=NO
FINAL_STATUS=PASS|ROLLED_BACK|BLOCKED
```

Do not report a repository as renamed until GitHub readback proves the same stable repository ID at the approved new full name. Do not report success while any inventoried integration is unresolved or the repository remains unintentionally frozen.
