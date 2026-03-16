from src.models import ReviewContext


def load_context(review_id: str, review_type: str = "pr") -> ReviewContext:
    """Load minimal context for local execution.

    In production this module should call GitHub/GitLab APIs and fetch:
    - changed files
    - unified diff
    - commit metadata
    """
    changed_files = [
        "src/payment_service.py",
        "src/auth/token_handler.py",
        "web/ui/profile.tsx",
    ]
    diff = """diff --git a/src/payment_service.py b/src/payment_service.py
+ query = f\"SELECT * FROM users WHERE id = {user_id}\"
+ cache = []
+ for item in big_list:
+     cache.append(process(item))
"""
    return ReviewContext(
        review_id=review_id,
        review_type=review_type,
        changed_files=changed_files,
        diff=diff,
    )
