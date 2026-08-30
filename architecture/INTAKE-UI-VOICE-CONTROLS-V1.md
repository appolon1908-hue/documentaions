# Codestra Intake UI and Voice Controls v1

## Purpose

Define the reusable application-facing layer for forms, surveys, callbacks, popups, and voice controls without creating alternate authentication, routing, CRM, or telephony control planes.

## Canonical application path

`site UI -> intake-form / intake-survey / intake-voice-controls -> intake-sdk / communication voice transport -> same-origin BFF -> Caddy -> Kong -> Middleware -> durable processing -> Odoo / analytics / permitted workflows`

## UI authority

`@codestra/intake-ui` owns framework-neutral accessible render models, submit state, popup behavior, callback controls, and DOM mounting helpers. It must not hold service credentials, choose Odoo models, or create privileged connector commands.

## Voice authority

`@codestra/intake-voice-controls` owns browser microphone permission, start, mute/unmute, end, accessible session status, and voice-session UI lifecycle.

Realtime audio transport is injected through the `VoiceTransport` interface. The communication/voice SDK owns WebRTC/provider-specific media and signaling. Intake voice controls own the website UX and intake context only.

## Credential boundary

Browser code must not receive Keycloak confidential client secrets, SIP credentials, telephony provider API keys, direct Kong credentials, direct Middleware credentials, or Odoo credentials. Browser control requests use a same-origin server boundary. Public API control traffic must continue through Caddy then Kong before Middleware.

## Campaign and CRM context

Voice controls may carry tenantId, siteId, campaignId, conversationId, locale, and approved metadata. These are descriptive inputs. Middleware remains responsible for tenant authorization, campaign mapping, CRM association, durable events, and downstream writes.

## Calling boundary

The voice-control package does not itself authorize PSTN dialing. Production dialing remains governed by the communication/telephony control plane, runtime capability flags, campaign policy, and server-side authorization. Adding a Start Voice button must never turn on live PSTN delivery.

## Accessibility

Controls must expose semantic buttons, keyboard operation, live status via ARIA, explicit microphone states, mute state, connection state, and recoverable errors. Forms/surveys must preserve labels, required-state semantics, validation messages, and keyboard navigation.

## Supported presentation surfaces

- embedded forms
- landing-page forms
- multi-step surveys
- modal/popup forms
- callback widgets
- post-call surveys
- customer-service surveys
- voice start/mute/end controls
- chat/voice combination widgets through separate channel adapters

## Release rule

UI and voice-control code may be merged only after exact-head workspace/type/test gates pass. Runtime deployment, Keycloak provisioning, Kong apply, Caddy reload, Odoo write enablement, and production telephony activation require their own reviewed release gates.
