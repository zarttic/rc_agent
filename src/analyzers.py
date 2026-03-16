def run_static(context: dict) -> list:
    """Run static analyzers and return unified issues."""
    return []


def run_ai(context: dict, enabled: bool = True) -> list:
    """Run AI analysis and return unified issues."""
    if not enabled:
        return []
    return []
