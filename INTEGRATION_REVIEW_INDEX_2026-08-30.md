# Codestra canonical integration review index — 2026-08-30

## Purpose

This index identifies the exact source changes that resolve the Odoo,
Middleware and n8n contract conflicts. It is a review guide, not deployment or
activation authority.

## Accepted architecture decision

```text
AUTOMATION_AUTHORITY = Middleware adopts /v2/automation/*
CROSS_SYSTEM_WRITER  = Middleware only
ORCHESTRATOR         = n8n
BUSINESS_AUTHORITY   = Odoo 19
CANONICAL_CRM_TYPE   = crm.lead.upsert
CRM_VERSION          = "1.0"
ODOO_WRITE           = false
EXTERNAL_EFFECTS     = false
```

Canonical routes:

```text
n8n -> Middleware
POST /v2/automation/commands
GET  /v2/automation/commands/{command_id}

Middleware -> Odoo
POST /codestra/middleware/v1/commands/crm.lead.upsert
GET  /codestra/middleware/v1/commands/{command_id}/status
```

The n8n `/v1/integrations/n8n/*` routes and the Odoo direct CRM CRUD routes are
deprecated compatibility aliases. They are not canonical for new work.

## Reviewed source baselines

| Repository | Baseline used for replacement branch | Replacement branch |
|---|---:|---|
| `appolon1908-hue/Odoo` | `16356fa57fbda080fe78831507eccd63d9a00fc4` | `fix/canonical-integration-contract-v2-20260830` |
| `appolon1908-hue/Middleware-` | `0227e9d0380bf4808540d61c6f168fee584d138c` | `fix/odoo-canonical-command-v2-20260830` |
| `appolon1908-hue/N8N` | `20d86c9de07db361fc183e32ba6c0c2069b1e5f6` | `fix/canonical-automation-contract-v2-20260830` |
| `appolon1908-hue/Infustruction-repo` | `273395b07e2eba1111c9e2f6a80bf8384d104cfb` | `decision/middleware-automation-v2-odoo-command-20260830` |
| `appolon1908-hue/communication-platform-` | `6d9c1be678d2c1e78f99d94b14bbf47d5b9a417a` | `docs/canonical-cross-system-control-plane-20260830` |
| `appolon1908-hue/documentaions` | `95c203f9bd0aa76bcf13e922c277e5beac27f92e` | `docs/canonical-integration-review-index-20260830` |

## Required review order

### Review group A — business and transport contract

1. **Odoo canonical integration contract**
   - real bridge name: `codestra_middleware_bridge`;
   - one canonical upsert command and status route;
   - exact signed-header order;
   - unknown-outcome reconciliation;
   - deprecated direct-CRUD aliases;
   - `ODOO_WRITE=false`.

2. **Middleware canonical Odoo adapter**
   - uses `crm.lead.upsert` only;
   - uses command-status read-back;
   - signs tenant, correlation and idempotency headers;
   - one Temporal write attempt;
   - shared synthetic HMAC vector;
   - no live capability activation.

These two reviews should be evaluated together for byte compatibility. Neither
should be production-enabled by merging it.

### Review group B — automation contract and disabled consumers

3. **n8n automation-v2 contract**
   - thirteen canonical operations;
   - one v2 command submit/read pair;
   - exact client-family scopes;
   - string `command_version = "1.0"`;
   - `crm.lead.upsert` Odoo template;
   - claimed job and lease context;
   - v1 routes rejected in new templates;
   - inactive, disabled, credential-free source exports.

This review can occur in parallel with group A, but final source merge must not
proceed until the shared control-plane JSON and command contract agree.

### Review group C — architecture authorities

4. `Infustruction-repo`: accepted ADR.
5. `communication-platform-`: canonical communications/CRM control plane.
6. `documentaions`: this index and final PR links.

Documentation describes the reviewed source decision. It cannot override a
failing code check or grant deployment authority.

## Cross-repository invariants reviewers must confirm

- Middleware is the only cross-system writer.
- n8n calls Middleware only.
- Odoo accepts the canonical resource-specific command only for new CRM work.
- Tenant and requester assertions match the verified token and durable job.
- No generic execute or command scope exists.
- The HMAC field order is identical in Odoo and Middleware.
- The synthetic HMAC vector digest is identical in Odoo and Middleware.
- A timeout never causes automatic write resubmission.
- Odoo command status is read before a retry decision.
- All workflows remain inactive and HTTP command nodes remain disabled.
- No runtime credential, HMAC secret, database secret or customer data is in Git.
- `ODOO_WRITE` and all external-effect capabilities remain false.

## Known runtime gaps that are not disguised as source conflicts

The complete thirteen-route Middleware automation-v2 runtime is still an
implementation workstream. The Middleware conformance waiver register remains
binding until each route lands with its tests. These gaps must not be described
as fixed merely because source contracts now agree.

Staging certification also remains required for:

- exact Keycloak client, audience and scope configuration;
- Kong route and mTLS behavior;
- Odoo module upgrade against a sanitized restore;
- timeout-after-commit reconciliation;
- duplicate and semantic-conflict behavior;
- backup, restore and rollback;
- immutable artifact, SBOM, provenance and signing;
- write-disabled canary and soak evidence.

## Superseded open pull-request families

The following historical PRs contain useful material but conflict with current
main, duplicate newer modules, or declare obsolete contract names. They should
not be merged unchanged:

### Odoo

```text
#2   historical Middleware-only architecture bootstrap
#3   historical Keycloak contract with adapter-source-missing state
#9   obsolete canonical addon import snapshot
#44  duplicate communications authority documentation
#49  marketing contract that can be read as a second Odoo writer
#50  overlapping intake upsert branch based before the merged marketing CRM foundation
#52  repository profile containing incorrect visibility/branching statements
```

### n8n

```text
#25  useful v2 direction but based on stale main and incomplete envelope alignment
```

### Middleware

Historical design/authority PRs should be compared against the replacement
adapter PR before being closed. Product or provider implementation PRs are not
superseded merely because this control-plane contract changed.

A superseded PR should receive a comment naming the replacement review before
closure. Unique fixes must be ported or explicitly disposed; they must not be
silently discarded.

## Merge and deployment prohibition

This index authorizes review only. It does not authorize:

- merging with administrator bypass;
- enabling auto-deploy;
- changing a server;
- activating n8n;
- enabling Odoo writes;
- installing or upgrading Odoo modules;
- enabling email, SMS, social, crawler, callback, VICIdial or PSTN effects;
- deleting historical branches without a disposition record.

The final review links and check status will be appended after the six pull
requests are opened.
