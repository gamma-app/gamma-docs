# Connector tracker

Lightweight status tracker for every Gamma connector known to the OAuth stack. One row per connector. The [MCP access requests sheet](https://docs.google.com/spreadsheets/d/1S7wuQ1oEGEJhpobMz_6CRWUgsnCjFQoa65YFYjtVuGs/edit?gid=497166213#gid=497166213) is authoritative for pending requests; this file is authoritative for what's actually live on `main`.

## Status vocabulary

Connectors move through these stages left to right:

1. `requested` — submitted via form, not yet reviewed
2. `approved (sheet)` — Byron approved in the sheet; eligible for the next batch PR
3. `PR drafted` — code change drafted, awaiting review
4. `PR merged` — merged to `main`, but not yet live
5. `terraform applied` — allowlist deployed to prod; connector can register via DCR
6. `live` — fully working end-to-end; users can authorize
7. `App Host enabled` — (optional) connector can render generation previews inline via `generation-details.guard.ts`

## Live connectors

All rows default to `live` — they're merged and applied. Update the status column when something changes.

| Connector | Client type | Status | PR(s) | Notes |
| --- | --- | --- | --- | --- |
| Atlassian | `atlassian` | live | [#15319](https://github.com/gamma-app/gamma/pull/15319) (logo), [#15679](https://github.com/gamma-app/gamma/pull/15679) (typed classification) | |
| Glean | `glean` | live + App Host | [#15379](https://github.com/gamma-app/gamma/pull/15379) (logo), [#15679](https://github.com/gamma-app/gamma/pull/15679) (typed + suffix), [#16724](https://github.com/gamma-app/gamma/pull/16724) (App Host) | Uses `-be.glean.com` hostname suffix match. |
| ChatGPT | `chatgpt` | live + App Host | [#15679](https://github.com/gamma-app/gamma/pull/15679) (typed), [#15484](https://github.com/gamma-app/gamma/pull/15484) (App Host), [#16599](https://github.com/gamma-app/gamma/pull/16599) (multi-host) | Multi-host: `chatgpt.com`, `platform.openai.com`, `[^/]+.chatgpt.com`, `oauth.tools`. |
| Claude | `claude` | live + App Host | [#15679](https://github.com/gamma-app/gamma/pull/15679) (typed), [#15849](https://github.com/gamma-app/gamma/pull/15849) (App Host) | |
| Superhuman | `superhuman` | live | [#15756](https://github.com/gamma-app/gamma/pull/15756) | Maps from `coda.io` hostname. |
| Grok | `grok` | live | [#18152](https://github.com/gamma-app/gamma/pull/18152) (typed + logo), [#18376](https://github.com/gamma-app/gamma/pull/18376) (Terraform patterns), [#18473](https://github.com/gamma-app/gamma/pull/18473) (regex tweak) | Multi-host: `grok.com`, `console.x.ai`. Terraform patterns landed with the PS→TF migration, not the main onboarding PR. |
| Lantern | `lantern` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Peripheral | `peripheral` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1), [#18885](https://github.com/gamma-app/gamma/pull/18885) (URI correction) | URIs corrected after resubmission in batch 2. |
| Maybe | `maybe` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Ledgers | `ledgers` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Needle | `needle` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Actava | `actava` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Algora | `algora` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Rockhood | `rockhood` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Code and Theory | `codetheory` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | Multi-host: `stagwell-machine.com` + `dev.*` + `stage.*` env variants. |
| Rubica | `rubica` | live | [#18530](https://github.com/gamma-app/gamma/pull/18530) (batch 1) | |
| Veleiro | `veleiro` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| MissionSquad | `missionsquad` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| SheetXAI | `sheetxai` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| Optimizely | `optimizely` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| Auglab | `auglab` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| DesignGrow | `designgrow` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| Mimasa | `mimasa` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| Fireflies | `fireflies` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | Four callback hosts: `askfred.*`, `app.fireflies.ai`, `next.fireflies.dev`, + one more. |
| Worklayer | `worklayer` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |
| Elvin | `elvin` | live | [#18885](https://github.com/gamma-app/gamma/pull/18885) (batch 2) | |

## Pending / in-flight

Add rows here as you work the sheet. Status should be `requested`, `approved (sheet)`, `PR drafted`, or `PR merged`. Move to the live table above once `terraform applied` and the auth flow verifies end-to-end.

| Connector | Client type (proposed) | Status | PR(s) | Notes |
| --- | --- | --- | --- | --- |
| _none tracked yet_ | | | | |

## How to keep this honest

- **After every batch PR merges:** update the relevant rows here; bump status to `PR merged` → `terraform applied` → `live` as each step confirms.
- **When working the sheet:** any row approved by Byron but not yet in the live table → add as `approved (sheet)` in the pending section.
- **When a connector requests App Host access:** that's a separate decision (flag to eng leadership); bump the live row to `live + App Host` only after the `generation-details.guard.ts` PR merges.
- **When in doubt:** the [pr-catalog.md](pr-catalog.md) is the authoritative history of what shipped. This file is a convenience index on top of it.
