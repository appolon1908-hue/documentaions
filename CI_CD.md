# CI/CD authority

## Repository

- Repository: `appolon1908-hue/documentaions`
- Class: `documentation`
- Purpose: Codestra architecture, integration, governance, and operating documentation
- Runtime authority: none

## Persistent branches

```text
development
test
staging
production
main
```

Documentation promotion order:

```text
docs/fix -> development -> test -> staging -> production -> main
```

The initial bootstrap places the same CI/CD policy on all persistent branches. It does not assign application or production authority.

## Required CI

`.github/workflows/required-ci.yml` runs on every branch push, pull request, and manual dispatch. It proves exact source identity, runs a checksum-verified Gitleaks scan, rejects unsafe escaping symlinks and oversized files, parses JSON and YAML, verifies local Markdown links, and uploads sanitized evidence.

## Every-branch audit

`.github/workflows/all-branches-audit.yml` runs daily and manually. It fetches every branch tip and validates each in an isolated worktree, so older documentation branches are covered without rewriting history.

## Continuous delivery

`.github/workflows/continuous-delivery.yml` runs only on the persistent branch train. It creates a deterministic documentation source archive, records the exact Git SHA/tree and SHA-256 checksums, and uploads 90-day immutable release evidence.

This repository has no runtime. Continuous delivery therefore ends at the checksummed documentation artifact. It does not publish containers, change websites, contact servers, modify configuration, or authorize external effects.

## Required GitHub settings

Protect `development`, `test`, `staging`, `production`, and `main` or apply equivalent rulesets. Require `required-ci`, approving review, resolved conversations, linear history, no force pushes, no deletion, and an up-to-date head before promotion.
