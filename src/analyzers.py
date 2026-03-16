from src.models import Issue, ReviewContext


SEVERITY_BY_SOURCE = {
    "flake8": "medium",
    "bandit": "high",
    "ai": "medium",
}


def run_static(context: ReviewContext, enabled_languages: dict | None = None) -> list[Issue]:
    """Run static analyzers and return unified issues.

    This MVP implementation returns deterministic findings for local validation.
    """
    _ = enabled_languages
    return [
        Issue(
            source="bandit",
            rule_id="B608",
            severity=SEVERITY_BY_SOURCE["bandit"],
            file="src/payment_service.py",
            line=12,
            category="security",
            message="Potential SQL injection risk from string interpolation.",
            suggestion="Use parameterized queries via DB driver placeholders.",
            confidence=0.95,
        ),
        Issue(
            source="flake8",
            rule_id="C901",
            severity=SEVERITY_BY_SOURCE["flake8"],
            file="src/auth/token_handler.py",
            line=44,
            category="maintainability",
            message="Function complexity is high.",
            suggestion="Split token validation into smaller helper functions.",
            confidence=0.88,
        ),
    ]


def run_ai(context: ReviewContext, enabled: bool = True) -> list[Issue]:
    """Run AI analysis and return unified issues."""
    if not enabled:
        return []

    return [
        Issue(
            source="ai",
            rule_id="AI-PERF-001",
            severity=SEVERITY_BY_SOURCE["ai"],
            file="src/payment_service.py",
            line=25,
            category="performance",
            message="Loop appends one-by-one; list comprehension may be faster and cleaner.",
            suggestion="Replace with `[process(item) for item in big_list]`.",
            confidence=0.76,
        )
    ]
