# Security Baseline

- Redact secrets before sending context to external models.
- Send minimal diff-first context.
- Keep CI tokens in secret manager only.
- Provide local-only mode (`ai.enabled=false`).
- Store auditable request IDs for model calls.
