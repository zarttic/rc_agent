import json
from pathlib import Path

from src.models import Issue, ReviewReport


def build_report(review_id: str, issues: list[Issue]) -> ReviewReport:
    summary = {
        "total": len(issues),
        "high": sum(1 for item in issues if item.severity == "high"),
        "medium": sum(1 for item in issues if item.severity == "medium"),
        "low": sum(1 for item in issues if item.severity == "low"),
    }
    return ReviewReport(review_id=review_id, summary=summary, issues=issues)


def to_markdown(report: ReviewReport) -> str:
    lines = [
        f"# Review Report ({report.review_id})",
        "",
        f"- Total issues: {report.summary['total']}",
        f"- High: {report.summary['high']}",
        f"- Medium: {report.summary['medium']}",
        f"- Low: {report.summary['low']}",
        "",
        "## Findings",
    ]

    for issue in report.issues:
        lines.extend(
            [
                f"- **[{issue.severity.upper()}]** `{issue.file}:{issue.line}` ({issue.source}/{issue.rule_id})",
                f"  - Category: {issue.category}",
                f"  - Message: {issue.message}",
                f"  - Suggestion: {issue.suggestion}",
            ]
        )

    return "\n".join(lines) + "\n"


def write_outputs(report: ReviewReport, output_dir: str) -> tuple[str, str]:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    json_path = out_path / "report.json"
    md_path = out_path / "report.md"

    json_path.write_text(
        json.dumps(report.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    md_path.write_text(to_markdown(report), encoding="utf-8")

    return str(json_path), str(md_path)
