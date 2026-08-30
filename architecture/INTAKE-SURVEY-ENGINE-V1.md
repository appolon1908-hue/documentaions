# Codestra Intake Survey Engine v1

## Canonical path

`survey UI -> @codestra/intake-survey -> @codestra/intake-sdk -> same-origin @codestra/intake-bff -> Caddy -> Kong -> Middleware -> durable inbox/outbox -> Odoo / analytics / permitted workflows`

Survey traffic uses the same authenticated intake edge as industry forms. Caddy and Kong do not interpret survey answers as authorization. Middleware remains the routing/write authority.

## Responsibilities

`@codestra/intake-survey` owns versioned survey definitions, question validation, branching visibility, anonymous-mode policy, expiration, response construction and survey-specific metadata. It does not own credentials, tenants, Odoo models or connector methods.

## Response model

Survey answers remain survey-response data. Middleware may associate a survey response with an existing contact, lead, campaign or service event, but full survey answers should not be flattened into `crm.lead` fields. Odoo or an analytics store should use a dedicated survey-response model when persistence is required.

## Supported v1 question types

Single choice, multiple choice, rating, NPS, yes/no, text, textarea and matrix are part of the contract. Conditional visibility may depend on prior answers. Definitions are immutable by `(surveyId, version)` once released.

## Anonymous responses

Anonymous mode is opt-in per survey definition. When anonymous mode is active, the SDK must not include contact or lead identifiers in the response metadata. Tenant/site/campaign routing identifiers remain required platform context and are not respondent identity.

## Sensitive-data boundary

Public surveys are not general protected-data collection forms. Government identifiers, passwords, bank/card credentials, credit reports, medical records, diagnoses and similar regulated or high-risk fields require a separately reviewed protected workflow. Dynamic survey configuration must not bypass this boundary.

## Analytics

NPS/CSAT calculations are derived analytics and do not change raw responses. Raw responses remain the source of truth. Aggregates should be reproducible from versioned definitions and raw response events.

## Release gates

Before release: package build/typecheck/tests must pass; exact-head SDK CI and compatibility gates must be green; anonymous-mode and sensitive-field tests must pass; form/BFF layers must already be validated; and no runtime deployment or live-write capability is authorized by this document.
