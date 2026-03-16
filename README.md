# Code Review Agent

A Codex-ready starter that now includes a product plan + runnable local review pipeline.

## What is included
- Product docs: PRD, roadmap, API contract, runbook
- CI templates: GitHub Actions + GitLab CI
- Config templates with schema
- Local review pipeline that generates JSON/Markdown artifacts

## Quick start
1. Install deps:
   - `pip install -r requirements.txt`
2. Generate a local report:
   - `python scripts/review_agent.py --pr 101 --config config/default.json --output-dir artifacts`
3. Simulate posting PR comments:
   - `python scripts/post_comments.py --pr 101 --report artifacts/report.json`

## Productization docs
- `docs/prd.md`
- `docs/roadmap.md`
- `docs/api-contract.md`
- `docs/runbook.md`

## Repository layout
See `docs/project-structure.md`.
