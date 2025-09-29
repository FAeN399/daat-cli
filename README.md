
# Starter Project — Sharp 60‑Minute Kickoff

This repo gives you a **universal start window** for most projects (software, research, ops, content). By minute 60 you’ll have: a one‑page brief, CI placeholder, issue/PR templates, a 9‑item backlog, and a 48‑hour test.

## Quickstart (10 minutes)
1. Duplicate or clone this folder and rename it.
2. Fill out [`PROJECT_BRIEF.md`](./PROJECT_BRIEF.md) (keep it to one page).
3. Create a new repo: `git init && git add . && git commit -m "chore: init starter" && git branch -M main`.
4. Create a remote and push (GitHub example):
   ```bash
   gh repo create <org>/<name> --public --source=. --push
   # or: git remote add origin git@github.com:<org>/<name>.git && git push -u origin main
   ```
5. Open a board with columns: **Backlog → Ready → In Progress (WIP 2) → Review → Done**.

## The 60‑Minute Start Window
**00–05 — Name & North Star**: 1‑sentence problem & outcome; 3‑bullet DoD.  
**05–10 — Measure & Guardrails**: primary metric + counter‑metric; constraints.  
**10–20 — People & Decision Path**: DACI roles; comms channel/time; where ADLs/ADRs live.  
**20–35 — Risks & First Bet**: pick #1 assumption; design the smallest 48h test + kill criteria.  
**35–50 — Repo & Workflow**: commit templates; enable CI; WIP=2; create 9‑item backlog (3/3/3).  
**50–60 — Commit & Calendar**: assign 48h test; schedule T+48h checkpoint; share links.

### 48‑Hour Loop
- **T+24h:** 10‑min check (is the test running? blockers?)
- **T+48h decision:** Keep (scale), Adjust (re‑scope), or Stop (write a short note).

## Files & Folders
- `PROJECT_BRIEF.md` — one‑page brief template.
- `.github/ISSUE_TEMPLATE/task.md` — 1‑day vertical slice issue.
- `.github/pull_request_template.md` — PR checklist.
- `.github/workflows/ci.yml` — minimal CI placeholder.
- `DECISIONS/0001-example-adr.md` — ADR template/example.
- `CODEOWNERS` — add reviewers or ownership per path.
- `docs/60-minute-start-window.md` — printable runbook.
- `forge.yaml` — optional minimal Forge config (if you use Master Forge MCP).
- `LICENSE` — MIT.
- `SECURITY.md` — report vulnerabilities.
- `.gitignore` — common ignores.

## Conventions
- 1‑page brief, 1‑day tasks, **WIP ≤ 2**, daily 10‑minute stand‑up.
- Every user‑visible change behind a **feature flag**.
- Decide once, log once (ADR); revisit only with new data.
- Celebrate **learning** (including killed ideas), not volume.

---

**Happy shipping.**
