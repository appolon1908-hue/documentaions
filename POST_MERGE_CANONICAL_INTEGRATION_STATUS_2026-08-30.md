# Codestra canonical integration — merged source status

**Date:** 2026-08-30  
**Scope:** Odoo, Middleware, n8n, identity/gateway dependencies, and architecture authority  
**Runtime activation:** not authorized

## Merged review set

The canonical source-contract repair was reviewed through:

- `appolon1908-hue/Odoo` PR #53;
- `appolon1908-hue/Middleware-` PR #71;
- `appolon1908-hue/N8N` PR #34;
- `appolon1908-hue/Infustruction-repo` PR #17;
- `appolon1908-hue/communication-platform-` PR #5;
- `appolon1908-hue/documentaions` PR #5.

These merges replace competing route, command, HMAC, retry, and architecture definitions with one source authority.

## Canonical interfaces

```text
n8n -> Middleware
POST /v2/automation/commands
GET  /v2/automation/commands/{command_id}

Middleware -> Odoo
POST /codestra/middleware/v1/commands/crm.lead.upsert
GET  /codestra/middleware/v1/commands/{command_id}/status
```

```text
command_type    = crm.lead.upsert
command_version = "1.0"
target          = odoo-19
capability      = ODOO_WRITE
```

Middleware is the only cross-system writer. Odoo remains the CRM/business system of record. n8n is an orchestration client. Kong is the authenticated routing boundary. Keycloak is the machine-identity and exact-scope authority.

## Security and reliability invariants

- Tenant and requester assertions never grant authority by themselves.
- The verified Keycloak token and durable job/command records are authoritative.
- No generic execute scope or unrestricted Odoo model proxy is allowed.
- Odoo and Middleware sign timestamp, event ID, method, path, tenant, correlation ID, idempotency key, and raw body in the same order.
- Exact replay returns the original result.
- Changed-content reuse of the same identity fails closed.
- A timeout is an unknown outcome and triggers status reconciliation before any retry decision.
- Middleware performs one destination-write attempt; n8n does not automatically repeat an unknown write.
- Multi-tenant production requires tenant-specific HMAC secrets and service identities; the legacy global fallback is not tenant-isolated.

## Source versus runtime status

```text
CANONICAL_SOURCE_CONTRACT_MERGED=YES
RUNTIME_INTEGRATION_CERTIFIED=NO
ODOO_MODULE_RECONCILED_TO_GITHUB=NO
ALL_AUTOMATION_V2_ROUTES_CERTIFIED=NO
KEYCLOAK_RUNTIME_CLIENTS_VERIFIED=NO
KONG_RUNTIME_POLICY_VERIFIED=NO
STAGING_TIMEOUT_RECONCILIATION_PROVED=NO
PRODUCTION_ACTIVATION_AUTHORIZED=NO

ODOO_WRITE=false
LIVE_WRITE=false
ENABLE_EXTERNAL_DELIVERY=false
LIVE_SMS_DELIVERY=false
LIVE_EMAIL_DELIVERY=false
LIVE_PSTN_DIALING=false
PRODUCTION_DIALING=DISABLED
```

## Next source workstreams

1. Rework Odoo PR #50 from current protected `main`; retain only unique intake requirements and use the merged canonical bridge.
2. Complete and certify the Middleware automation-v2 runtime operation set, removing waivers one route at a time with persistence, authorization, lease, concurrency, and reconciliation tests.
3. Version the exact Keycloak machine-client, audience, scope, token-lifetime, tenant, and service-account plan.
4. Version the exact Kong route, authentication, mTLS/private-network, request-limit, timeout, and egress plan.
5. Prepare an isolated Odoo staging reconciliation plan using a sanitized database/filestore restore and exact protected SHAs.
6. Prepare timeout-after-commit, duplicate, semantic-conflict, cross-tenant, restore, and rollback certification evidence.

## Promotion prohibition

No merged document or source branch activates a workflow, enables a provider effect, changes an Odoo database, deploys a server, grants a credential, or authorizes production. Each activation requires its own exact-artifact review and approval.
