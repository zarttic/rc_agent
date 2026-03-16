# Security Baseline

## Data minimization
- Prefer diff-first analysis; avoid sending full repository when unnecessary.
- Exclude ignored paths and binary/generated files.

## Secret hygiene
- Mask known secret patterns before AI requests.
- Keep API tokens in CI secret manager only.
- Avoid logging raw tokens or full request payloads.

## Access control
- Use least-privilege PAT/app tokens for GitHub/GitLab APIs.
- Restrict comment bot permissions to target repositories.

## Auditability
- Record request ID, model name, token usage, and outcome.
- Persist report artifacts for incident investigation.

## Fallback mode
- Support `ai.enabled=false` for static-only analysis in sensitive repos.
