# Report Format

## Artifact outputs
- `artifacts/report.json`: machine-readable report
- `artifacts/report.md`: human-readable summary for PR comments

## Unified issue model
```json
{
  "source": "flake8|bandit|ai",
  "rule_id": "E501",
  "severity": "high|medium|low",
  "file": "src/a.py",
  "line": 10,
  "category": "security|performance|maintainability|quality",
  "message": "...",
  "suggestion": "...",
  "confidence": 0.91
}
```

## Summary model
```json
{
  "total": 3,
  "high": 1,
  "medium": 2,
  "low": 0
}
```
