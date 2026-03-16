import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.analyzers import run_ai, run_static
from src.config_loader import load_config
from src.context_loader import load_context
from src.report_generator import build_report, write_outputs
from src.report_merger import merge_issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Run code review pipeline")
    parser.add_argument("--pr", help="GitHub pull request number")
    parser.add_argument("--mr", help="GitLab merge request IID")
    parser.add_argument("--config", default="config/default.json")
    parser.add_argument("--output-dir", default="artifacts")
    args = parser.parse_args()

    if not args.pr and not args.mr:
        raise SystemExit("Either --pr or --mr is required")

    review_id = args.pr or args.mr
    review_type = "pr" if args.pr else "mr"

    config = load_config(args.config)
    ai_enabled = bool(config.get("ai", {}).get("enabled", True))

    context = load_context(review_id=review_id, review_type=review_type)
    static_issues = run_static(context, enabled_languages=config.get("languages", {}))
    ai_issues = run_ai(context, enabled=ai_enabled)
    merged_issues = merge_issues(static_issues, ai_issues)

    report = build_report(review_id=review_id, issues=merged_issues)
    json_path, md_path = write_outputs(report, args.output_dir)

    print(f"Generated {report.summary['total']} issues for {review_type.upper()} #{review_id}")
    print(f"JSON report: {json_path}")
    print(f"Markdown report: {md_path}")


if __name__ == "__main__":
    main()
