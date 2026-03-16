from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class Issue:
    source: str
    rule_id: str
    severity: str
    file: str
    line: int
    message: str
    suggestion: str = ""
    confidence: float = 0.8
    category: str = "quality"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ReviewContext:
    review_id: str
    review_type: str
    base_branch: str = "main"
    head_branch: str = "feature"
    changed_files: list[str] = field(default_factory=list)
    diff: str = ""


@dataclass
class ReviewReport:
    review_id: str
    summary: dict[str, Any]
    issues: list[Issue]

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["issues"] = [issue.to_dict() for issue in self.issues]
        return payload
