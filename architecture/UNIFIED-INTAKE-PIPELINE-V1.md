# Codestra Unified Intake Pipeline v1

## Canonical path

`website / landing page / form / chat / voice -> @codestra/intake-sdk -> same-origin BFF -> Caddy -> Kong -> Middleware -> durable inbox/outbox -> Odoo`

This order is mandatory. Intake traffic must not skip Caddy, Kong, or Middleware.

## Repository authority

- `appolon1908-hue/SDK-repository`: browser/server intake contract and reusable SDK.
- `appolon1908-hue/Caddy`: public HTTPS/TLS reverse-proxy edge for `api.codestra.co`; forwards `/v1/intake*` to Kong.
- `appolon1908-hue/Kong`: API gateway route, authentication, rate limits, body limits and gateway policy.
- `appolon1908-hue/Keycloak`: confidential `sdk-intake` service identity with narrow `leads.write` access and `middleware-api` audience.
- `appolon1908-hue/Middleware-`: canonical `POST /v1/intake/leads`, tenant enforcement, durable event identity, idempotency, Odoo command mapping and cross-system write authority.
- `appolon1908-hue/Odoo`: private CRM upsert implementation invoked through the Middleware-managed connector.

## Request contract

Public intake requests reach `POST /v1/intake/leads` only after Caddy and Kong. Required service identity: `sdk-intake`. Required scope: `leads.write`. Required headers: `Authorization`, `X-Tenant-ID`, `X-Correlation-ID`, and `Idempotency-Key`.

Browser code must never store the `sdk-intake` secret or a reusable service credential. A same-origin BFF obtains a short-lived client-credentials token.

## Durable processing

Middleware records `codestra.events.lead_submitted`. New requests return accepted semantics; exact retries are duplicate-safe; reuse of an idempotency identity with a changed semantic payload is a conflict. Odoo delivery is asynchronous/guarded and must remain subject to the `ODOO_WRITE` capability and existing connector read-back/reconciliation rules.

## Odoo mapping

Middleware emits the internal command `crm.lead.intake.upsert.v1` to target `odoo-19`. Odoo's `codestra_intake_leads` module provides `crm.lead.codestra_upsert_intake_lead` behavior without exposing a public Odoo intake endpoint. Identity precedence is event/idempotency identity first, then existing active CRM lead matching by normalized email or phone inside the same tenant.

## Prohibited paths

The following are architecture violations:

- browser -> Middleware directly with a service secret;
- browser -> Kong while bypassing the site BFF credential boundary;
- Caddy -> Middleware for `/v1/intake*` while bypassing Kong;
- Kong -> Odoo for lead intake;
- site/BFF -> Odoo directly;
- n8n -> Odoo as a replacement for Middleware write authority;
- enabling Odoo live writes from an SDK, Caddy or Kong repository change.

## Release gates

Before production activation, all involved PR heads must pass their repository CI. Keycloak client provisioning and Kong route application must be reviewed. Caddy routing must validate. Middleware exact-head tests must prove authentication, tenancy, limits, duplicate behavior and conflict behavior. Odoo module tests/install validation must pass. An end-to-end no-effect test should prove the full edge path while live write capabilities remain disabled.

This document describes architecture only and does not authorize runtime deployment.
