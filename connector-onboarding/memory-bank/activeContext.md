# Active Context

## Current focus

Establishing this sub-directory and memory bank as the durable record of the onboarding process. First pass — refine after next session of actual onboarding work. Nothing is in-flight on the sheet as tracked here yet; a sheet review is the first real use of this folder.

## Recent changes

- PR #18885 (batch 2) merged 2026-04-17 — 10 new connectors live
- PR #18530 (batch 1) merged 2026-03-30 — 10 new connectors live, introduced the batch model
- PR #18376 earlier in March — moved the redirect URI allowlist from Parameter Store to Terraform
- This folder created `<this-session-date>` — first cut of `pr-catalog`, `process`, `connectors`, and memory bank

## Next steps

1. Walk the MCP access requests sheet and populate the "Pending / in-flight" section of `connectors.md` with anything approved but not yet merged
2. Decide whether to invest in automating the S3 logo upload (Matt flagged interest; no owner yet)
3. Consider a post-merge nudge (Slack bot or GitHub Action) to ping eng for Terraform apply after each batch
4. Validate that the batch cadence is working for Matt and Byron — if not, revisit
5. Next time an onboarding session runs, confirm `process.md` still matches Matt's Notion doc; flag drift if found

## Active decisions and considerations

- **Batch cadence.** Weekly-ish per Matt and Byron's earlier conversation, but unconfirmed steady-state. Revisit after the next 2-3 batches.
- **App Host inclusion.** Case-by-case per the skill. Currently ChatGPT, Claude, Glean. No new candidates flagged.
- **S3 automation vs status quo.** Cost of manual upload is low per connector but adds up across batches. Nothing scheduled.
- **Whether this memory bank should pull from the sheet directly.** Today it's a manual mirror. Automating would be nice but risks stale data if the automation breaks silently.

## Important patterns and preferences

- Stealth surgeon scope for all onboarding PRs — 3 files, minimal diff, match existing conventions in `oauth-client-type.ts` and `prod.tfvars`
- Never merge an onboarding PR without confirming the logo is in S3 first
- Never claim a connector is live until Terraform apply confirms end-to-end auth works
- Skill approval gate is non-negotiable — "Byron approved in sheet" must be verified before any code change

## Learnings and insights

- The 3-file pattern is genuinely stable. Variations are in hostname matching (exact vs suffix) and host count (single vs multi).
- Glean's `-be.glean.com` suffix rule is the most interesting edge case — if a new connector has tenant subdomains, look here first.
- The Parameter Store → Terraform migration (#18376) was high-impact: it turned the allowlist into reviewable code but introduced Terraform apply as a new manual step
- `git log --follow` on `oauth-client-type.ts` is noisy because of off-main branches; always filter to `main` when auditing
