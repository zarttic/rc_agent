# Metrics

## Quality KPIs
- Suggestion adoption rate = accepted suggestions / total suggestions
- False positive rate = rejected findings / total findings
- Reopen rate after merge (proxy for missed issues)

## Performance KPIs
- P50/P95 review latency per PR
- Pipeline success rate
- Static-only fallback rate

## Cost KPIs
- Token usage per PR
- Model spend per PR and per repository

## Stage targets
- MVP: P95 < 8 min, fallback rate < 20%
- v1: P95 < 5 min, fallback rate < 10%
- v2: P95 < 3 min, fallback rate < 5%
