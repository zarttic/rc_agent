# API/Data Contracts

## Input contract (review run)
```json
{
  "review_id": "123",
  "review_type": "pr",
  "repo": "org/repo",
  "base_branch": "main",
  "head_branch": "feature/x",
  "changed_files": ["src/a.py"],
  "diff": "..."
}
```

## Unified issue contract
```json
{
  "source": "bandit",
  "rule_id": "B608",
  "severity": "high",
  "file": "src/payment_service.py",
  "line": 12,
  "category": "security",
  "message": "Potential SQL injection risk",
  "suggestion": "Use parameterized queries",
  "confidence": 0.95
}
```

## Output contract (report)
```json
{
  "review_id": "123",
  "summary": {"total": 3, "high": 1, "medium": 2, "low": 0},
  "issues": []
}
```
