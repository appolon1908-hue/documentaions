# Staging Intake E2E Certification Plan — 2026-08-30

## Objective

Certify the unified intake path in staging without enabling production or uncontrolled external effects:

`test client -> staging Caddy -> staging Kong -> staging Middleware -> durable inbox/outbox -> Odoo connector boundary`

Forms, surveys, callbacks and voice-control commands must use the same edge/security architecture. Voice media itself remains outside this intake-control certification and must not activate PSTN calling.

## Hard stop conditions

Abort before the first request if any of the following is not provably false/disabled:

- production/live writes
- production Odoo writes
- n8n external delivery
- email external delivery
- SMS external delivery
- production PSTN dialing
- production Caddy/Kong/Keycloak mutation

Do not silently downgrade a missing safety assertion into a warning.

## Phase A — configuration/read-back

Record exact source/deployed SHAs and read back staging configuration for Caddy, Kong, Middleware and the Odoo connector. Confirm:

1. Caddy is the only public intake edge and forwards `/v1/intake*` to Kong.
2. Kong routes lead and survey intake only to Middleware.
3. `sdk-intake` requires the correct audience and narrow scopes.
4. Middleware has `POST /v1/intake/leads` and `POST /v1/intake/surveys/responses`.
5. Middleware external-effect flags remain disabled.
6. Odoo has no public intake controller.
7. Odoo write execution remains disabled for the no-effect phase.

Any configuration drift is a NO-GO until reconciled to Git authority.

## Phase B — gateway/security negative tests

Prove fail-closed behavior for:

- no bearer token
- expired/invalid token
- wrong audience
- wrong client
- missing `leads.write`
- missing `surveys.write`
- missing tenant header
- token/header tenant mismatch
- missing correlation ID
- missing idempotency key
- oversized body
- Kong rate limit
- attempted direct Middleware public bypass
- attempted direct Odoo intake bypass

Expected behavior is explicit authentication/authorization/validation rejection, never framework 404 caused by a missing canonical route.

## Phase C — lead no-effect positive path

Submit a synthetic, non-sensitive staging lead with unique tenant/site/campaign and deterministic idempotency/correlation identities.

Require evidence that:

1. Caddy accepted the public staging path.
2. Kong authenticated and forwarded the request.
3. Middleware returned an accepted receipt.
4. the durable inbox contains the canonical lead event.
5. retry with the same idempotency identity returns duplicate semantics and does not create a second event.
6. same idempotency identity with changed semantic payload returns conflict.
7. Odoo connector command generation is observable but no live Odoo write occurs in Phase C.
8. no n8n/email/SMS/voice external effect occurs.

## Phase D — survey no-effect positive path

Submit both an identified synthetic survey response and an anonymous response.

Require evidence that:

- the dedicated survey route/scope is used;
- anonymous payloads cannot carry contact/lead identifiers;
- durable survey events remain distinct from CRM lead fields;
- duplicate/conflict behavior matches the durable idempotency contract;
- no live Odoo write or external effect occurs.

## Phase E — optional isolated Odoo staging-write certification

This phase is NOT implied by Phase A-D success. It requires an explicit staging-write approval and an isolated test Odoo database/tenant.

If approved, temporarily enable only the staging Odoo connector write capability required for the test, while production and every unrelated external-effect flag remain disabled.

Prove:

- create of a synthetic CRM lead;
- same-event replay is idempotent;
- same-tenant normalized email/phone matching behaves as designed;
- cross-tenant matching is impossible;
- survey data is not flattened indiscriminately into CRM columns;
- rollback/delete of synthetic test records is documented;
- write capability is returned to disabled state and read back afterward.

## Evidence packet

Capture, without secrets or PII:

- timestamp
- environment
- exact repository/deployed SHAs for Caddy, Kong, Middleware, Odoo and Keycloak desired state
- request correlation/idempotency test IDs
- HTTP statuses and bounded response summaries
- gateway and Middleware sanitized logs
- durable inbox/outbox evidence
- Odoo connector no-effect evidence or isolated staging-write evidence
- final read-back of all safety flags
- PASS/FAIL for each gate

## Certification decision

Only declare `STAGING_INTAKE_E2E=PASS` when every required Phase A-D gate is green on the same reviewed staging configuration.

Phase E, if executed, receives a separate `STAGING_ODOO_WRITE=PASS|FAIL` decision.

Neither decision authorizes production deployment, live delivery or PSTN calling.
