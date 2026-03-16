# Code Review Agent

A Codex-ready scaffold for building an automated PR/MR code review agent.

## MVP scope
- CI trigger from GitHub/GitLab
- Diff/context loading
- Static analysis orchestration
- AI analysis orchestration
- Unified report generation
- PR/MR feedback posting

## Quick start
1. Copy `.env.example` to `.env` and set API keys.
2. Adjust `config/default.yaml` rules.
3. Run `python scripts/review_agent.py --help`.

## Repository layout
See `docs/project-structure.md`.
