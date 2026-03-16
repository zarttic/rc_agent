# Architecture

## End-to-end flow
1. CI Trigger receives PR/MR event.
2. Context Loader fetches diff + metadata + dependency files.
3. Static analyzers run in parallel by language.
4. AI analyzer runs on filtered diff/context.
5. Result Merger deduplicates and resolves conflicts.
6. Report Generator emits Markdown/JSON/HTML.
7. Feedback module posts inline + summary comments.

## Failure & fallback
- Static analyzer failure: mark warning and continue.
- AI timeout: fallback to static-only report.
- API posting failure: save report artifact for manual upload.
