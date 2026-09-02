# Codestra Intake BFF v1

## Purpose

The BFF is the server-only credential boundary between public website code and the Codestra edge. Every Codestra-managed website, landing page, form, chat widget, callback widget, or voice capture flow should submit through its own same-origin BFF route.

Canonical flow:

`browser -> @codestra/intake-sdk -> same-origin @codestra/intake-bff -> Caddy -> Kong -> Middleware -> durable inbox/outbox -> Odoo`

## Server-only identity

The BFF uses Keycloak client credentials for `sdk-intake` and requests `leads.write`. The client secret must stay in server secret storage and must never appear in JavaScript delivered to a browser, source maps, public runtime config, HTML, logs, telemetry, or Git.

The service token is short-lived and may be cached only in server memory for less than its remaining validity. A 401 may trigger one forced refresh.

## Request controls

The BFF must require and preserve:

- `X-Tenant-ID`
- `X-Correlation-ID`
- `Idempotency-Key`
- `Content-Type: application/json`

The body `tenantId` must exactly match `X-Tenant-ID`. Each deployed website should configure an explicit tenant allowlist. The default payload ceiling is 1 MiB. Responses must be non-cacheable.

## Retry rules

Retries are allowed only for retry-safe gateway conditions such as `429`, `502`, `503`, and `504`, plus a single token refresh after `401`. The exact same `Idempotency-Key`, `X-Correlation-ID`, tenant ID, and body must be preserved across attempts. The BFF must never invent a second lead identity during a retry.

## Public edge

The BFF sends only to the Caddy-owned public API URL `https://api.codestra.co/v1/intake/leads`. It must not use a Middleware container/private address. Caddy forwards the intake path to Kong, Kong enforces identity/scope/rate/body controls, and Middleware remains the business/write authority.

## Prohibited behavior

- browser-held `sdk-intake` secret;
- browser-held reusable service bearer token;
- BFF -> Middleware private network bypass;
- BFF -> Odoo;
- BFF -> n8n as the primary lead write path;
- changing `X-Tenant-ID` during retry;
- retrying with a new idempotency key;
- logging access tokens or client secrets.

## Repository implementation

Implementation authority: `appolon1908-hue/SDK-repository`, package `@codestra/intake-bff`, branch `feature/intake-bff-v1` stacked on `feature/unified-intake-sdk-v1`.

Runtime deployment is not authorized by this document.
