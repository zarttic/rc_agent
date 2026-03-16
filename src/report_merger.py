from src.models import Issue


SEVERITY_RANK = {"high": 0, "medium": 1, "low": 2}


def merge_issues(static_issues: list[Issue], ai_issues: list[Issue]) -> list[Issue]:
    """Merge, deduplicate, and sort issues.

    Deduplication key: (file, line, category, normalized_message)
    Static issues are preferred when duplicate keys exist.
    """
    merged: dict[tuple[str, int, str, str], Issue] = {}

    for issue in static_issues + ai_issues:
        key = (
            issue.file,
            issue.line,
            issue.category,
            issue.message.strip().lower(),
        )
        if key not in merged:
            merged[key] = issue
            continue

        existing = merged[key]
        if existing.source == "ai" and issue.source != "ai":
            merged[key] = issue

    return sorted(
        merged.values(),
        key=lambda item: (
            SEVERITY_RANK.get(item.severity, 99),
            item.file,
            item.line,
        ),
    )
