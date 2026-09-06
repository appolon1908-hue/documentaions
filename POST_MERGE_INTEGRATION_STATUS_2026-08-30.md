# Codestra post-merge integration status — 2026-08-30

## Authority

This file replaces any conversational summary that stated all integration PRs
were merged before GitHub confirmed them. GitHub pull-request and exact-head
check state is authoritative.

## Canonical source decision

```text
AUTOMATION_CONTRACT = Middleware adopts /v2/automation/*
CROSS_SYSTEM_WRITER = Middleware only
ORCHESTRATOR = n8n
BUSINESS_SYSTEM_OF_RECORD = Odoo 19
CANONICAL_CRM_COMMAND = crm.lead.upsert
CANONICAL_CRM_COMMAND_VERSION = "1.0"
ODOO_WRITE = false
WORKFLOWS_ACTIVE = false
EXTERNAL_EFFECTS = false
```

Canonical boundaries:

```text
n8n -> Middleware
POST /v2/automation/commands
GET  /v2/automation/commands/{command_id}

Middleware -> Odoo
POST /codestra/middleware/v1/commands/crm.lead.upsert
GET  /codestra/middleware/v1/commands/{command_id}/status
```

## Confirmed merged repositories

| Repository | PR | Merge commit | Status |
|---|---:|---|---|
| `appolon1908-hue/Middleware-` | [#71](https://github.com/appolon1908-hue/Middleware-/pull/71) | `d9735422796cb2aa18a39339aad3cc87bdf67ba9` | MERGED |
| `appolon1908-hue/Infustruction-repo` | [#17](https://github.com/appolon1908-hue/Infustruction-repo/pull/17) | `d066cfaf605c54fe321c342d986aa7a6d2db9d8c` | MERGED |
| `appolon1908-hue/communication-platform-` | [#5](https://github.com/appolon1908-hue/communication-platform-/pull/5) | `5d08ddc6cf9326ba5f6305d05189893a352b230f` | MERGED |
| `appolon1908-hue/documentaions` | [#5](https://github.com/appolon1908-hue/documentaions/pull/5) | `476182a474d78e434021c1638295feee234c5a7e` | MERGED |

## Remaining source promotions

### Odoo PR #53

- Pull request: https://github.com/appolon1908-hue/Odoo/pull/53
- Exact head: `1274232ca5ab6d1fdfa2046651d95625d662a939`
- Merge conflict state: clean
- Security gate: passed
- All inline review threads: resolved
- Odoo Addons CI: exact-head rerun in progress at the time of this record
- Merge authorization: approved by the repository owner, but merge remains
  prohibited until all required exact-head and merge-result checks are green

### N8N PR #34

- Pull request: https://github.com/appolon1908-hue/N8N/pull/34
- Latest reconciled main included: `b63f9bedccf4f9b5c55ee673cd7c88caa88f2a74`
- Current exact head: `050c07639b87993a7f90a7874d367daba48c4e4b`
- Merge conflict state: clean
- Source validation: passed
- All inline review threads: resolved
- Community-runtime security from N8N PR #35 is retained
- Merge blocker: repository rule requires approval from someone other than the
  latest pusher; review requested from `kazan555`

## Source controls fixed

- real Odoo bridge name is `codestra_middleware_bridge`;
- new CRM ingestion uses `crm.lead.upsert` version `"1.0"`;
- Middleware signs tenant, correlation, idempotency and raw body identities;
- Odoo and Middleware share the same synthetic HMAC vector;
- timeout-after-write invokes command-status reconciliation before a retry
  decision;
- n8n templates use the lease-bound automation-v2 command envelope;
- deprecated v1 command paths are prohibited in new n8n templates;
- community-runtime route, editor, credential and egress controls are preserved;
- workflows and external-effect capabilities remain disabled.

## Runtime work still open

Source convergence is not runtime completion. The following remain separate,
reviewed implementation and certification gates:

1. implement and certify every missing Middleware automation-v2 runtime route;
2. provision exact Keycloak clients, audiences and scopes through protected
   configuration;
3. certify Kong routes, token forwarding, mTLS and private-service boundaries;
4. reconcile the installed Odoo modules with the exact protected source in a
   sanitized staging restore;
5. prove duplicate, concurrent, semantic-conflict and timeout-after-commit
   behavior end to end;
6. certify backup, restore, migration rollback, immutable images, SBOM,
   provenance and signatures;
7. run a write-disabled staging canary and soak test;
8. enable any live capability only through a separate approved change.

## Explicit non-actions

This status update does not activate n8n, install or upgrade Odoo modules,
change an Odoo database or filestore, provision credentials, deploy a runtime,
send email/SMS/social traffic, control VICIdial, place a PSTN call, or enable any
external write.
