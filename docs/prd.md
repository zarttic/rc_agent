# Product Requirements Document (PRD)

## 1. Product vision
Build a CI-native Code Review Agent that provides automated, actionable feedback for pull/merge requests with static + AI hybrid analysis.

## 2. Target users
- Individual developers who need fast feedback before human review
- Tech leads who want consistent engineering standards
- Engineering managers who need quality and delivery metrics

## 3. Core scenarios
1. Developer opens PR and receives findings in minutes.
2. Reviewer sees prioritized summary (High/Medium/Low) and concrete fix suggestions.
3. Team admin configures rules per repository/language.
4. Platform owner tracks historical trends in dashboard.

## 4. Functional requirements
- FR-1: Trigger on PR/MR events (open, synchronize, reopen)
- FR-2: Fetch diff + changed files + metadata
- FR-3: Run static analysis per language
- FR-4: Run AI analysis on minimal context
- FR-5: Merge results with deduplication/conflict policy
- FR-6: Output JSON + Markdown reports
- FR-7: Post inline/summary comments back to PR/MR
- FR-8: Support config overrides and local-only mode

## 5. Non-functional requirements
- NFR-1: P95 analysis time < 8 minutes (MVP target)
- NFR-2: Partial failure tolerance (degrade to static-only)
- NFR-3: Secret redaction and external-call auditability
- NFR-4: Multi-repo and multi-language extensibility

## 6. Success metrics
- Suggestion adoption rate
- False positive rate
- Median review turnaround reduction
- Cost per analyzed PR
