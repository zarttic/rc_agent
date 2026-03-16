from dataclasses import dataclass


@dataclass
class Issue:
    source: str
    rule_id: str
    severity: str
    file: str
    line: int
    message: str
    suggestion: str = ""
