# Intake + Voice Release Certification — 2026-08-30

## Scope

This certification covers the Codestra intake application stack and its companion platform authorities:

`site UI -> intake-form / intake-survey / intake-ui / intake-voice-controls -> intake-sdk -> same-origin intake-bff -> Caddy -> Kong -> Middleware -> Odoo / analytics / permitted workflows`

Realtime voice media remains owned by the communication/voice SDK through the injected `VoiceTransport`. Intake voice controls own browser UX and intake context only.

## Repository certification matrix

| Repository | PR / branch | Head reviewed | Evidence | Status |
| --- | --- | --- | --- | --- |
| SDK-repository | PR #34 `feature/intake-survey-v1` | `df8c459b3f5ab9cdd8c13a55c6b71e44215075e0` | Compatibility + Workspace CI green | CERTIFIED |
| SDK-repository | PR #35 `feature/intake-ui-v1` | `12b8352fe23b80b21e23aba0a9213d81f1be6e23` | Compatibility + Workspace CI green | CERTIFIED |
| SDK-repository | PR #36 `feature/intake-voice-controls-v1` | `992af9934ae76b50ef77a2479866aabcdf71680b` | Compatibility, Contract validation, Workspace CI, Middleware service, and Generated SDKs all green on exact head | CERTIFIED |
| Caddy | PR #8 `feature/intake-edge-route-v1` | `8a5b58c112600d3bb957b3cfad9a9285554f86f4` | Validate Caddy source authority green | CERTIFIED |
| Kong | PR #19 `feature/intake-gateway-route-v1` | `9b351e336a5e5841727e584c1557db41f15e1617` | Prior route/security suite passed; newest head has no attached Actions run | CONDITIONALLY CERTIFIED / CI EVIDENCE BLOCKED |
| Middleware | PR #54 `feature/unified-lead-intake-v1` | `cc6ae33b198c27ed192a84456a1784b5627e75bb` | Prior exact-head intake/connector validation green before later synchronization; newest head has no attached Actions run | CONDITIONALLY CERTIFIED / CI EVIDENCE BLOCKED |
| Keycloak | PR #32 `feature/sdk-intake-client-v2` | `dafda3d4be26ffdcd0964781964c5a81a1768bcf` | Previous head exposed MoneyBee creatable-client inventory mismatch; validator corrected to explicitly review `sdk-intake`; newest head requires fresh CI evidence | CONDITIONALLY CERTIFIED / CI REQUIRED |
| Odoo | PR #48 `feature/intake-lead-upsert-v1` | `40f462cfd2a3584963508ebdd177ee71782f0fab` | Odoo Addons CI + Security gates green | CERTIFIED |

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
10. No runtime apply, live Odoo write activation, PSTN dialing activation, or production deployment is certified by this document.

## Required release gates before merge/deployment

- SDK PR #36 exact-head certification is complete and must remain green on `992af9934ae76b50ef77a2479866aabcdf71680b` or be recertified after any head change.
- A fresh exact-head gateway validation must exist for Kong PR #19.
- A fresh exact-head Middleware validation must exist for PR #54.
- A fresh exact-head Keycloak GitOps validation must exist for PR #32 and must pass after the reviewed-inventory correction.
- All companion PRs must remain on the documented heads or be recertified after any code/config change.
- Merge the SDK stack in dependency order and retarget/rebase each next layer before merging it.
- Perform staging-only end-to-end validation through Caddy -> Kong -> Middleware -> Odoo with live external delivery and production calling disabled.

## Release decision

`GO_FOR_MERGE = NO`

`GO_FOR_STAGING_CERTIFICATION = YES, after Kong + Middleware + Keycloak exact-head evidence is green`

`GO_FOR_PRODUCTION = NO`

This is a repository/code certification record only. It is not a deployment authorization.
