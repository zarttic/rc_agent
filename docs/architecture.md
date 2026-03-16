# Architecture

## End-to-end flow
1. **CI Trigger** receives PR/MR event.
2. **Context Loader** fetches review metadata, changed files, and diff.
3. **Static Analyzers** execute language-specific checks.
4. **AI Analyzer** evaluates logic/perf/security/readability on minimal context.
5. **Report Merger** deduplicates findings and resolves source conflicts.
6. **Report Generator** emits JSON + Markdown artifacts.
7. **Feedback Publisher** posts summary/inline comments to PR/MR.

## Runtime components
- `scripts/review_agent.py`: orchestration entrypoint
- `src/context_loader.py`: fetch/context abstraction
- `src/analyzers.py`: static + AI analyzers abstraction
- `src/report_merger.py`: conflict/dedup strategy
- `src/report_generator.py`: output generation
- `scripts/post_comments.py`: PR/MR feedback publisher

## Failure & fallback policy
- Static analyzer failure: continue with surviving analyzers.
- AI failure/timeout: degrade to static-only report.
- Feedback API failure: persist artifacts for manual posting.

## Extensibility
- Add analyzer plugin adapters under `src/analyzers_*`.
- Add platform adapters for GitHub/GitLab APIs.
- Add async execution queue for large PR workloads.
