import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Post review comments to PR/MR")
    parser.add_argument("--pr")
    parser.add_argument("--mr")
    parser.add_argument("--report", default="artifacts/report.json")
    args = parser.parse_args()

    target = args.pr or args.mr
    target_type = "PR" if args.pr else "MR"

    report_path = Path(args.report)
    if not report_path.exists():
        raise SystemExit(f"Report file not found: {report_path}")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    summary = report.get("summary", {})

    print(
        f"Would post to {target_type} #{target}: "
        f"total={summary.get('total', 0)}, "
        f"high={summary.get('high', 0)}, "
        f"medium={summary.get('medium', 0)}, "
        f"low={summary.get('low', 0)}"
    )


if __name__ == "__main__":
    main()
