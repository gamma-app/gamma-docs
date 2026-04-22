# Project Brief

## Project

Iterating on Gamma's connector onboarding flow. Owner: Max Jackson (with Matt Carroll on the engineering side and Byron Jones on product approvals). Scope is the onboarding process itself — everything between "form submitted" and "connector live in production."

## Goal

Cut time-per-connector and time-per-batch. Keep the onboarding mechanical enough that it stays correct under time pressure, and keep session-to-session context in this folder so that no agent (or human) has to re-derive the process every time a new batch lands.

## Core Deliverables

- `pr-catalog.md` — authoritative history of every real onboarding PR vs lookalikes
- `process.md` — synthesis of skill + Matt's Notion + deltas since the original writeup
- `connectors.md` — lightweight status tracker, one row per connector
- A working batch PR cadence (weekly-ish) for approved connectors

## Scope

### In scope

- The onboarding process: 3-file pattern, redirect URI validation, logo mapping, Terraform allowlist
- Batch PR cadence + skill execution
- Sheet + Slack triage
- Status tracking across the full connector lifecycle

### Out of scope

- OAuth provider internals (owned by the platform eng team)
- App Host / `generation-details.guard.ts` decisions (case-by-case engineering decision, not default onboarding behavior)
- The connector's own OAuth client implementation (the connector's problem, not ours)
- Anything in `packages/mcp-server/` beyond what the skill's Step 3-5 touches

## Success criteria

- A new agent session in this folder can pick up the next batch in under 2 minutes of reading
- Every merged batch PR is reflected in `connectors.md` the same day
- No silent drift between the skill, Matt's Notion, and `process.md` — if there's drift, it's flagged
- Terraform apply is never forgotten after a merge (currently the highest-risk manual step)
