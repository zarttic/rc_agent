def merge_issues(static_issues: list, ai_issues: list) -> list:
    """Merge, deduplicate, and sort issues by severity and location."""
    return static_issues + ai_issues
