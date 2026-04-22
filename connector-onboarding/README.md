# Connector onboarding

Internal ops reference for iterating on Gamma's connector onboarding flow. **Not published** — this folder is deliberately absent from `SUMMARY.md` so GitBook does not render it. It exists so that agent sessions (and humans) can pick up where the last batch left off without re-deriving context.

## Contents

| File | What it is |
| --- | --- |
| [pr-catalog.md](pr-catalog.md) | Every connector-onboarding PR merged to `gamma` main, grouped and annotated. Source of truth for "what was a real onboarding" vs "what was a refactor". |
| [process.md](process.md) | Synthesis of Matt's Notion doc, the `onboard-connector` skill, and the architecture reference — with deltas since Matt wrote the original. |
| [connectors.md](connectors.md) | Lightweight status tracker: one row per connector, current lifecycle stage, linked PRs. |
| [memory-bank/](memory-bank/) | Six Cline-canonical files (`projectbrief`, `productContext`, `activeContext`, `systemPatterns`, `techContext`, `progress`) scoped to this sub-project. |

## How the memory bank is scoped

The memory bank in this folder is scoped to **this subdirectory**, not the whole `gamma-docs` repo. When running memory-bank skills here:

- `follow-memory-bank` — run from `connector-onboarding/` as the project root
- `update-memory-bank` — same, run after each batch PR or process change
- `create-memory-bank` — already run once to seed these files; do not re-run (it will refuse to clobber)

## How to use this folder

**Before starting a new batch:** read `connectors.md` (what's already live + what's pending) and `activeContext.md` (what you were working on last session).

**While writing a batch PR:** cross-reference `pr-catalog.md` to match commit conventions and confirm the 3-file pattern is still current. Use `process.md` for the step-by-step.

**After merging a batch PR:** update `connectors.md` rows to `PR merged` and flag for Terraform apply. Run `update-memory-bank` to bump `activeContext.md` and `progress.md`.

## Canonical external sources

- [Notion: Onboarding a new connector](https://www.notion.so/gamma-app/Onboarding-a-new-connector-327f3594899480b5b2e1e11c57f533db) — Matt's process doc
- [MCP access requests sheet](https://docs.google.com/spreadsheets/d/1S7wuQ1oEGEJhpobMz_6CRWUgsnCjFQoa65YFYjtVuGs/edit?gid=497166213#gid=497166213) — intake + Byron approval
- `#mcp-access-requests` Slack channel — triage
- `~/.claude/skills/onboard-connector/SKILL.md` — step-by-step skill
- `~/.claude/skills/onboard-connector/reference.md` — architecture reference

If anything in this folder drifts from those sources, those sources win.
