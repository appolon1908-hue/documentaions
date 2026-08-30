# Industry Intake Form Engine v1

## Authority

The public form engine lives in `appolon1908-hue/SDK-repository` as `@codestra/intake-form`.

Canonical path:

`website / landing page -> @codestra/intake-form -> @codestra/intake-sdk -> same-origin @codestra/intake-bff -> Caddy -> Kong -> Middleware -> durable inbox/outbox -> Odoo`

## Design rule

The infrastructure is shared across all industries. Industry differences are expressed as versioned, reviewed form definitions containing field descriptors, validation rules, consent requirements, prohibited public fields, industry identity and form type. Websites must not fork their own credential, gateway or CRM pipeline.

## v1 industries

General/contact, financial services, transportation/logistics, home services, medical transportation, software/services, real estate, insurance, education, nonprofit, and contact-center campaigns.

New industries are added as versioned definitions. They do not receive new public API paths unless a separate architecture review proves a different security boundary is required.

## Common envelope

Every form builds the same intake-compatible envelope: `tenantId`, `siteId`, `campaignId`, `source`, `submittedAt`, `formId`, common contact fields, consent, attribution, industry fields and metadata. Metadata includes the reviewed `intakeIndustry`, `intakeFormType` and `intakeFormVersion`.

## Public-data safety boundary

Public forms must collect only information appropriate for lead/contact/request intake. Sensitive data must use a separately reviewed protected workflow. The public registry rejects form definitions that mark fields as sensitive and v1 presets explicitly prohibit applicable fields such as SSNs/tax IDs, bank/card credentials, passwords, credit reports, medical records/diagnoses, medication/health-condition data and similar high-risk fields.

This is an architectural boundary, not a replacement for product-specific legal/compliance review.

## Routing

Industry/form metadata is descriptive input to Middleware routing. It does not allow the browser to choose an Odoo model, connector method or privileged destination. Middleware remains responsible for tenant/campaign routing and downstream write authority.

## Versioning

A published form definition is immutable in meaning. Material field, consent or validation changes require a new version. Sites may pin a version or follow a reviewed latest-version policy.

## Release gates

The form package must pass workspace build/typecheck/tests, prove prohibited-field rejection, prove required-consent behavior, prove industry metadata construction and remain compatible with `@codestra/intake-sdk`. The BFF, Caddy, Kong, Middleware and Odoo gates remain unchanged.

No deployment or live activation is authorized by this document.
