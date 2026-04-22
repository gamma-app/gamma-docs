# Product Context

## Why this exists

Connector onboarding was being re-derived each session. The process lives across four surfaces — Matt's Notion doc, the `onboard-connector` skill, the skill's architecture `reference.md`, and lived experience in PRs — and no one of them is sufficient on its own. Agents without the full picture were making predictable mistakes: treating refactor PRs as onboardings, forgetting the Terraform apply step, missing suffix-match edge cases for multi-tenant connectors.

## Problems it solves

- **Session-to-session memory.** Agents drop context between sessions; the memory bank carries it forward.
- **"Which PRs were real onboardings?"** The PR catalog separates onboardings from refactors, security hardening, and JWT/analytics work that incidentally touched the same files.
- **Stale sheet requests.** The pending section of `connectors.md` mirrors sheet state so approved connectors don't languish.
- **Forgotten Terraform apply.** The process explicitly calls out that merging the PR is necessary but not sufficient — an engineer still has to run `terraform apply`.
- **Inconsistent batch PRs.** The reference PRs (#18530, #18885) give the shape check so new batches stay mechanical.

## How it should work

A session starts. The agent reads `memory-bank/activeContext.md` to see what was in-flight last time, then scans `connectors.md` for sheet-approved rows without PRs. If there's enough to batch, the agent runs the `onboard-connector` skill in batch mode, drafts the PR, and updates `connectors.md` with `PR drafted`. Byron and an engineer review. On merge, the agent updates rows to `PR merged`, pings eng for Terraform apply, then bumps to `live` once verified. `activeContext.md` and `progress.md` get a one-line update after each batch.

## User experience goals

- **Low cost to resume.** Under 2 minutes of reading for an agent to pick up mid-stream.
- **Clear handoffs.** Every manual step (S3 upload, Terraform apply) is explicitly surfaced and doesn't depend on anyone remembering it.
- **Mechanical batches.** Approved connectors flow to a batch PR without improvisation.
- **Honest tracker.** `connectors.md` reflects reality; stale rows are a process failure to fix, not noise to ignore.

## Non-goals

- Not a replacement for Matt's Notion doc or the canonical skill — those remain authoritative
- Not a public-facing doc — intentionally absent from `SUMMARY.md`
- Not a per-connector knowledge base — per-connector detail lives in the PRs themselves, not here
- Not trying to automate approvals — that's Byron's call in the sheet, always
