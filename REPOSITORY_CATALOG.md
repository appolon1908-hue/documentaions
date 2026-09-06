# Codestra Repository Catalog

Metadata verified at `2026-09-06T16:49:16Z` for **58 accessible repositories** under `appolon1908-hue`. Visibility and default branches reflect that snapshot. Purpose descriptions are architecture classifications; they are not deployment or production-certification claims.

See [the continuation queue](REPOSITORY_CONTINUATION_2026-09-06.md) for every observed open issue and draft, and [the profile rollout](REPOSITORY_PROFILE_ROLLOUT.md) for verified profile presence. Current names remain operational until the controlled rename procedure is completed.

| # | Repository | Visibility | Default branch | Purpose / authority |
|---:|---|---|---|---|
| 1 | [`backend2`](https://github.com/appolon1908-hue/backend2) | `private` | `main` | **Corporate backend — Codestra CMS** — Django CMS/API serving website APIs, administration, media, health, and sitemap. Overlaps with `codestra-backend` and needs a canonical decision. |
| 2 | [`beyvra-backend`](https://github.com/appolon1908-hue/beyvra-backend) | `public` | `main` | **Product backend — trading platform** — Server-side API and business authority for the Beyvra FX/trading portal. Primary Beyvra trading backend authority. |
| 3 | [`beyvra-frontend`](https://github.com/appolon1908-hue/beyvra-frontend) | `public` | `main` | **Product frontend — trading platform** — Trading web application for markets, accounts, orders, positions, activity, funding, compliance, and operations. Primary Beyvra web frontend authority. |
| 4 | [`booked4seasons`](https://github.com/appolon1908-hue/booked4seasons) | `public` | `main` | **Product website — seasonal home services** — Public service-discovery and lead-capture website. Primary Booked4Seasons public website authority. |
| 5 | [`Breero.com`](https://github.com/appolon1908-hue/Breero.com) | `public` | `main` | **Product platform — home-services marketplace** — BREERO marketplace and field-service orchestration monorepo. Primary full-stack BREERO authority. |
| 6 | [`Caddy`](https://github.com/appolon1908-hue/Caddy) | `private` | `main` | **Platform edge — TLS and reverse proxy** — Public TLS, HTTP redirects, hostname routing, edge headers, and reverse-proxy configuration. |
| 7 | [`Codesrea-Social-`](https://github.com/appolon1908-hue/Codesrea-Social-) | `public` | `main` | **Platform control plane — social** — Intended provider-neutral social campaign, approval, publishing, engagement, and analytics control plane. Name requires review. |
| 8 | [`codestra`](https://github.com/appolon1908-hue/codestra) | `private` | `main` | **Corporate website and dashboard frontend** — Public Codestra website and authenticated dashboard built as a React application behind a TLS reverse proxy. Primary Codestra React frontend authority. |
| 9 | [`Codestra-AI`](https://github.com/appolon1908-hue/Codestra-AI) | `public` | `main` | **Platform control plane — AI** — Intended governed AI gateway for structured generation, provider routing, prompts, safety, evaluation, cost, and audit. |
| 10 | [`Codestra-Alertmanager`](https://github.com/appolon1908-hue/Codestra-Alertmanager) | `public` | `main` | **Observability backend — alert routing** — Grouping, deduplication, inhibition, silences, maintenance, and governed notification handoff. |
| 11 | [`Codestra-Alloy`](https://github.com/appolon1908-hue/Codestra-Alloy) | `public` | `main` | **Observability agent — Grafana Alloy** — Discovery, collection, processing, buffering, and forwarding for approved logs, metrics, and traces. |
| 12 | [`codestra-backend`](https://github.com/appolon1908-hue/codestra-backend) | `private` | `main` | **Corporate backend — recovered API** — Django API for the Codestra React frontend. Recovered Codestra backend whose authority must be reconciled with `backend2`. |
| 13 | [`Codestra-Blackbox-Exporter`](https://github.com/appolon1908-hue/Codestra-Blackbox-Exporter) | `public` | `main` | **Observability exporter — synthetic probes** — Side-effect-free HTTP/TCP/DNS/TLS/ICMP availability, latency, certificate, and content probes. |
| 14 | [`Codestra-cAdvisor`](https://github.com/appolon1908-hue/Codestra-cAdvisor) | `public` | `main` | **Observability exporter — container metrics** — Container CPU, memory, filesystem, network, I/O, throttling, OOM, and lifecycle metrics. |
| 15 | [`Codestra-Communication-CC`](https://github.com/appolon1908-hue/Codestra-Communication-CC) | `public` | `main` | **Platform control plane — communications** — Intended provider-neutral messaging control center for channels, templates, preferences, suppressions, status, and operator workflows. |
| 16 | [`codestra-foundation`](https://github.com/appolon1908-hue/codestra-foundation) | `private` | `main` | **Shared platform services** — Tenant, customer-profile, consent, subscription and entitlement authority; channel runtimes retain delivery ownership and Middleware remains the privileged integration boundary. |
| 17 | [`Codestra-Grafana-`](https://github.com/appolon1908-hue/Codestra-Grafana-) | `public` | `main` | **Observability UI — Grafana** — Operational dashboards, datasources, folders, and alert views. |
| 18 | [`Codestra-Loki`](https://github.com/appolon1908-hue/Codestra-Loki) | `public` | `main` | **Observability backend — logs** — Log ingestion, storage, retention, compaction, querying, tenancy, and label policy. |
| 19 | [`Codestra-Marketing-`](https://github.com/appolon1908-hue/Codestra-Marketing-) | `public` | `main` | **Platform control plane — marketing** — Intended campaigns, audiences, segments, creatives, approvals, scheduling, attribution, and performance control plane. |
| 20 | [`Codestra-Node-Exporter`](https://github.com/appolon1908-hue/Codestra-Node-Exporter) | `public` | `main` | **Observability exporter — host metrics** — Host CPU, memory, disk, filesystem, network, pressure, clock, hardware, and governed textfile evidence. |
| 21 | [`Codestra-OpenBao`](https://github.com/appolon1908-hue/Codestra-OpenBao) | `public` | `main` | **Platform security — secrets** — Secrets, policies, auth methods, OIDC, audit, integrated storage, HA, seal, backup, recovery, and DR. |
| 22 | [`Codestra-Postgres-Exporter`](https://github.com/appolon1908-hue/Codestra-Postgres-Exporter) | `public` | `main` | **Observability exporter — PostgreSQL** — Safe PostgreSQL health, locks, transactions, replication, WAL, checkpoints, vacuum, and capacity metrics. |
| 23 | [`codestra-production-platform`](https://github.com/appolon1908-hue/codestra-production-platform) | `private` | `release/production-activation` | **Platform reference and production evidence** — Coordinates production packaging, control-plane evidence, deployment instructions, and cross-component activation material. Reference/evidence package; not a replacement for principal component repositories. |
| 24 | [`codestra-production-runtime-authority`](https://github.com/appolon1908-hue/codestra-production-runtime-authority) | `private` | `main` | **Private runtime source authority** — Reviewed application source and vendor deployment configuration with source manifests and release evidence; merging does not authorize deployment. |
| 25 | [`Codestra-Prometheus`](https://github.com/appolon1908-hue/Codestra-Prometheus) | `public` | `main` | **Observability backend — metrics** — Scrape configuration, metrics storage, recording rules, alert rules, retention, and relabeling. |
| 26 | [`codestra-provisioning-service`](https://github.com/appolon1908-hue/codestra-provisioning-service) | `private` | `main` | **Platform service — provisioning** — Controlled provisioning and lifecycle management for campaigns, tenants, integrations, and platform resources. |
| 27 | [`Codestra-Redis-Exporter`](https://github.com/appolon1908-hue/Codestra-Redis-Exporter) | `public` | `main` | **Observability exporter — Redis** — Aggregate Redis availability, clients, memory, evictions, latency, replication, RDB, and AOF health. |
| 28 | [`Codestra-Telemetry`](https://github.com/appolon1908-hue/Codestra-Telemetry) | `public` | `main` | **Observability pipeline — OpenTelemetry** — OTLP receivers, processing, batching, redaction, sampling, retry, and exports. |
| 29 | [`Codestra-Tempo`](https://github.com/appolon1908-hue/Codestra-Tempo) | `public` | `main` | **Observability backend — traces** — Distributed trace ingestion, storage, retention, querying, and correlation. |
| 30 | [`Codestraxxxx`](https://github.com/appolon1908-hue/Codestraxxxx) | `private` | `main` | **Unclassified placeholder** — Reserved repository with no committed implementation or authoritative documentation. No production authority established. |
| 31 | [`communication-platform-`](https://github.com/appolon1908-hue/communication-platform-) | `public` | `main` | **Cross-repository architecture — communications** — Unified email/SMS/voice architecture, ownership, API model, lifecycle, dashboards, and release coordination. |
| 32 | [`Database-migrations-`](https://github.com/appolon1908-hue/Database-migrations-) | `public` | `main` | **Database migration source** — Review-gated migration packages for Appolon-owned services; production application requires separate authorization. |
| 33 | [`documentaions`](https://github.com/appolon1908-hue/documentaions) | `public` | `main` | **Cross-repository documentation** — Platform architecture, ownership maps, standards, governance, release sequencing, and reference documentation. |
| 34 | [`Frontend-Resturant-`](https://github.com/appolon1908-hue/Frontend-Resturant-) | `private` | `main` | **Product application — restaurant frontend** — Nuxt-based restaurant customer and operations frontend with reservations, orders, kitchen, tables, payments, waitlist, and tenant-scoped realtime updates. Primary frontend authority for the restaurant application. |
| 35 | [`Infustruction-repo`](https://github.com/appolon1908-hue/Infustruction-repo) | `public` | `main` | **Platform infrastructure and GitOps** — Shared topology, environments, networking, observability infrastructure, backups/DR, manifests, and infrastructure governance. |
| 36 | [`Keycloak`](https://github.com/appolon1908-hue/Keycloak) | `private` | `main` | **Platform security — identity** — Realms, clients, roles, scopes, audiences, authentication, MFA, sessions, recovery, and protected identity GitOps. |
| 37 | [`klyrow-Website-`](https://github.com/appolon1908-hue/klyrow-Website-) | `private` | `main` | **Public website — Klyrow** — Klyrow public marketing, legal, onboarding, and customer-facing website frontend. |
| 38 | [`klyrow.com`](https://github.com/appolon1908-hue/klyrow.com) | `public` | `main` | **Communications runtime — email** — Postal/Mautic/FastAPI email operations, domains, deliverability, suppressions, consent, journeys, analytics, and billing foundations. Primary email runtime authority. |
| 39 | [`Kong`](https://github.com/appolon1908-hue/Kong) | `private` | `main` | **Platform edge — API gateway** — API routes, services, plugins, rate limits, request validation, mTLS, and gateway policy. |
| 40 | [`kyqra`](https://github.com/appolon1908-hue/kyqra) | `public` | `main` | **Legacy crawler repository** — Historical Kyqra crawler/scraper source. Deprecated; canonical authority is `kyqra-crawler`. |
| 41 | [`kyqra-crawler`](https://github.com/appolon1908-hue/kyqra-crawler) | `public` | `main` | **Runtime service — canonical crawler** — Crawl-job API, queue, workers, persistence, dashboard, result storage, and signed callbacks. Canonical crawler authority. |
| 42 | [`LARIM-A-Backend`](https://github.com/appolon1908-hue/LARIM-A-Backend) | `private` | `main` | **Product backend — LARIMÍA marketplace** — Booking, provider, dispatch, visits, payments, realtime, audit, and workers. |
| 43 | [`LARIM-A-Fornt-end`](https://github.com/appolon1908-hue/LARIM-A-Fornt-end) | `public` | `main` | **Product frontend — LARIMÍA marketplace** — Customer web/mobile, professional mobile, and operations web workspace. |
| 44 | [`Middleware-`](https://github.com/appolon1908-hue/Middleware-) | `public` | `main` | **Platform control plane — integration and writes** — Authentication, tenancy, policy, idempotency, inbox/outbox, retries, reconciliation, audit, and adapters. Only privileged cross-system write authority. |
| 45 | [`Moneybee-Backend`](https://github.com/appolon1908-hue/Moneybee-Backend) | `public` | `main` | **Product backend — business funding** — MoneyBee applications, underwriting, matching, offers, documents, funding, compliance, and integrations. Primary backend/data authority. |
| 46 | [`Moneybee-frontend-`](https://github.com/appolon1908-hue/Moneybee-frontend-) | `public` | `main` | **Product frontend — business funding** — MoneyBee marketing site plus borrower, lender, and operations portals. Primary MoneyBee frontend authority. |
| 47 | [`N8N`](https://github.com/appolon1908-hue/N8N) | `public` | `main` | **Platform orchestration — workflows** — Business and integration workflows, schedules, routing, and operational automation. |
| 48 | [`Odoo`](https://github.com/appolon1908-hue/Odoo) | `public` | `main` | **Business system — CRM and ERP** — CRM, campaigns, contacts, opportunities, workflows, reporting, and custom modules. Primary business-state authority. |
| 49 | [`scrapper`](https://github.com/appolon1908-hue/scrapper) | `public` | `main` | **Legacy crawler lineage** — Historical multi-tenant business website crawler and CRM-enrichment service retained for migration evidence. `kyqra-crawler` is canonical. |
| 50 | [`SDK-repository`](https://github.com/appolon1908-hue/SDK-repository) | `public` | `main` | **Developer platform — contracts and SDKs** — Canonical OpenAPI/AsyncAPI, generated SDKs, webhook helpers, connectors, compatibility gates, and developer docs. Single shared SDK authority. |
| 51 | [`social.codestra.co`](https://github.com/appolon1908-hue/social.codestra.co) | `public` | `main` | **Product platform — social publishing** — Postiz-based publishing, scheduling, approvals, account connections, engagement, and analytics. |
| 52 | [`Superset`](https://github.com/appolon1908-hue/Superset) | `public` | `main` | **Analytics UI — Apache Superset** — Read-only, tenant-safe datasets, charts, dashboards, and row-level security. |
| 53 | [`telnexa`](https://github.com/appolon1908-hue/telnexa) | `private` | `main` | **Communications runtime — SMS** — Jasmin/SMPP/HTTP SMS gateway, callbacks, billing wallets, ledgers, usage, quotas, and operations. Primary Telnexa SMS runtime authority. |
| 54 | [`Telnexa-web`](https://github.com/appolon1908-hue/Telnexa-web) | `private` | `main` | **Public website — Telnexa** — Telnexa marketing, compliance, conversion, privacy, support, and service-onboarding frontend. |
| 55 | [`transportaion-Frontend`](https://github.com/appolon1908-hue/transportaion-Frontend) | `public` | `main` | **Product frontend — freight brokerage** — Broker, operations, admin, customer, and carrier applications. Primary freight frontend authority. |
| 56 | [`transportation-backend-`](https://github.com/appolon1908-hue/transportation-backend-) | `public` | `main` | **Product backend — freight brokerage** — Freight quoting, carriers, shipments, dispatch, tracking, documents, finance, integrations, and operations. Primary freight backend authority. |
| 57 | [`Vicidialer-Codestra`](https://github.com/appolon1908-hue/Vicidialer-Codestra) | `private` | `main` | **Communications runtime — voice/contact center** — VICIdial/Asterisk campaigns, agents, queues, callbacks, dispositions, recordings, and transfers. |
| 58 | [`Websocket-`](https://github.com/appolon1908-hue/Websocket-) | `public` | `main` | **Agent realtime gateway** — Authorized call-state and screen-pop transport using one-use tickets from Middleware; excludes SIP signaling and audio. |

## Rules

- Every repository must maintain `REPOSITORY_PROFILE.md`.
- Principal repositories own their runtime; documentation and infrastructure repositories must not duplicate application source.
- `SDK-repository` is the single shared SDK and contract authority.
- Middleware is the only privileged cross-system write authority.
- Legacy, duplicate, placeholder, and unclassified repositories must be labeled.
- Documentation updates do not deploy services or enable live effects.

## Consolidation decisions

- Canonical crawler: `kyqra-crawler`; `kyqra` and `scrapper` are legacy/migration repositories.
- SMS runtime: `telnexa`; website: `Telnexa-web`.
- Email runtime: `klyrow.com`; website: `klyrow-Website-`.
- Existing social application: `social.codestra.co`; proposed control plane: `Codesrea-Social-`.
- `codestra-backend` and `backend2` require a canonical/deprecation decision.
- `codestra-production-platform` is reference/evidence only.
- `Codestraxxxx` has no production authority.
