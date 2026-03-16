# Configuration

`config/default.json` controls rule switches, severity mapping, analyzer behavior, and output paths.

## Precedence
1. Global defaults (`config/default.json`)
2. Repo-local overrides (`config/repo.yaml`, optional future)
3. CI environment variable overrides (future)

## Key settings
- `ai.enabled`: enable/disable AI analysis
- `ai.model`: model name used by AI engine
- `languages.<lang>.enabled`: language pipeline switch
- `languages.<lang>.tools`: static tools per language
- `ignore.paths`: glob paths excluded from analysis

## Example
```yaml
ai:
  enabled: false
languages:
  python:
    enabled: true
```
