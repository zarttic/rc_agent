def load_context(pr_or_mr_id: str) -> dict:
    """Load diff and minimal repository context for analysis."""
    return {"id": pr_or_mr_id, "diff": "", "files": []}
