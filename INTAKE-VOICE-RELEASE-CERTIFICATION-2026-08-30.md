# Intake + Voice Release Certification — 2026-08-30

## Scope

This certification covers the Codestra intake application stack and its companion platform authorities:

`site UI -> intake-form / intake-survey / intake-ui / intake-voice-controls -> intake-sdk -> same-origin intake-bff -> Caddy -> Kong -> Middleware -> Odoo / analytics / permitted workflows`

Realtime voice media remains owned by the communication/voice SDK through the injected `VoiceTransport`. Intake voice controls own browser UX and intake context only.

## Current repository state

| Repository | Release state | Evidence / blocker |
| --- | --- | --- |
| SDK-repository | Foundation, BFF and industry form engine merged to `main` | merge SHAs `b61efcf4a88cb90a3e4c195a9b2558c6502c488c`, `534e8772f11fecdb6b831daa0fec96679121bf87`, `89810e4a74e7e8547c883da3962f8792233ded89` |
| SDK survey/UI/voice | Certified heads retained; clean release rebasing still required after squash-history divergence | survey `df8c459b3f5ab9cdd8c13a55c6b71e44215075e0`; UI `12b8352fe23b80b21e23aba0a9213d81f1be6e23`; voice `992af9934ae76b50ef77a2479866aabcdf71680b` |
| Middleware | MERGED to `main` | intake runtime PR #58 merged as `4aff2dffe1a92e89bbd6ee524a56aa11d47fe53c`; protected no-effect staging certification PR #62 merged as `1ad04aa614981f896b81d461bcc6c7dccd7d693f`; exact-head CI green |
| Odoo | Release PR #50 open | exact reviewed head `40f462cfd2a3584963508ebdd177ee71782f0fab`; fresh Odoo Addons CI + Security gates green; merge blocked by unresolved review/comments and independent last-push approval; reviewer requested |
| Kong | Release PR #28 open | head `9b351e336a5e5841727e584c1557db41f15e1617`; reviewed route/security suite reached 98/98 and deterministic manifests were certified on the certification branch; native release-head PR run still required before merge |
| Caddy | Release PR #9 open | head `8a5b58c112600d3bb957b3cfad9a9285554f86f4`; source authority previously green; keep public edge last in the release order |
| Keycloak managed identity authority | Release PR #39 open | exact head `93bf3e98b2a6fcd954524cbb2afb36fa02b2aefc`; `validate-source` and `validate-merge-result` green; protected `main` requires independent approval/CODEOWNERS/last-push approval and has no bypass |
| Keycloak sdk-intake | Certified intended tree | certification run succeeded on `a886eb7ca8adf911ad02690e476b4a2b99a25ab0`; promote only after managed identity authority is merged; no live realm apply authorized |

## Staging certification harness

Middleware `main` now contains `.github/workflows/staging-intake-e2e-no-effect.yml` from merge `1ad04aa614981f896b81d461bcc6c7dccd7d693f`.

The workflow is `workflow_dispatch` only, restricted to `main`, uses the protected environment `intake-staging-certification`, and requires:

- `base_url`: HTTPS staging Caddy public API endpoint
- `tenant_id`: synthetic staging tenant
- `runtime_readback`: exactly `ALL_EXTERNAL_EFFECTS_DISABLED`
- environment secret `STAGING_SDK_INTAKE_TOKEN`

The job sets and preserves:

- `LIVE_WRITES=false`
- `ODOO_WRITE=false`
- `N8N_DELIVERY_ENABLED=false`
- `LIVE_SMS_DELIVERY=false`
- `LIVE_EMAIL_DELIVERY=false`
- `LIVE_PSTN_DIALING=false`

The current ChatGPT GitHub connector can read and merge repository content but does not expose GitHub Environment/Secret mutation or `workflow_dispatch`. Therefore the protected environment/token cannot be bound and the manual staging run cannot be dispatched from this connector. No staging execution is claimed until those GitHub-side prerequisites are configured through an authorized GitHub UI/CLI/API path.

## Certified architecture invariants

1. Public intake must traverse Caddy before Kong.
2. Kong is the authenticated gateway and must not route directly to Odoo.
3. Middleware remains the cross-system write authority.
4. Browser code never receives confidential Keycloak, Kong, Middleware, Odoo, SIP, or provider credentials.
5. Forms and surveys use versioned schemas and reject prohibited public sensitive-data fields.
6. Anonymous survey responses cannot carry contact or lead identity.
7. Voice controls do not authorize PSTN calling and do not replace the communication/voice media engine.
8. Lead and survey writes preserve tenant, correlation, and idempotency identity across retries.
9. Odoo intake remains private and idempotent; no public Odoo intake controller is authorized.
10. Repository merge is not runtime deployment authorization.

## Controlled release order

1. Keycloak managed identity authority PR #39 after independent approval.
2. Keycloak `sdk-intake` desired state after the managed authority is on `main` and recertified against that exact base.
3. Middleware source authority — COMPLETE.
4. Middleware staging no-effect certification harness — COMPLETE.
5. Odoo release PR #50 after independent approval and resolved review threads.
6. Kong release PR #28 after native exact-head gateway validation.
7. Caddy release PR #9 last, after Kong source is accepted.
8. Rebuild and merge clean SDK survey -> UI -> voice release branches after current `main` squash ancestry is normalized.
9. Bind protected staging environment/token and execute Phase A–D no-effect certification.
10. Perform a separately approved isolated Odoo staging-write phase only after the no-effect path is green.

## Release decision

`GO_FOR_SOURCE_MERGE = PARTIAL`

`GO_FOR_STAGING_NO_EFFECT_CERTIFICATION = BLOCKED_ON_ENVIRONMENT_BINDING_AND_DISPATCH`

`GO_FOR_ODOO_STAGING_WRITES = NO`

`GO_FOR_PRODUCTION = NO`

This is a repository/code certification record only. It is not a deployment authorization.
