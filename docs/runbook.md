# Runbook

## Local dry-run
1. Install dependencies:
   - `pip install -r requirements.txt`
2. Generate report:
   - `python scripts/review_agent.py --pr 101 --config config/default.json --output-dir artifacts`
3. Simulate posting comments:
   - `python scripts/post_comments.py --pr 101 --report artifacts/report.json`

## Common failures
- Missing config file: check `--config` path.
- Missing report.json: run `review_agent.py` first.
- CI secret issues: verify token scopes and masked secrets.
