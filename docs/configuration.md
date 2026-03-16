# Configuration

`config/default.yaml` controls rule switches, severity mapping, and ignore patterns.

## Precedence
1. Global defaults
2. Repo-local config
3. CI environment overrides

## Example
```yaml
languages:
  python:
    enabled: true
```
