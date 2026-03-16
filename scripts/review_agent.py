import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
from src.context_loader import load_context
from src.analyzers import run_static, run_ai
from src.report_merger import merge_issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr")
    parser.add_argument("--mr")
    args = parser.parse_args()

    review_id = args.pr or args.mr
    context = load_context(review_id)
    static_issues = run_static(context)
    ai_issues = run_ai(context, enabled=True)
    issues = merge_issues(static_issues, ai_issues)
    print(f"Generated {len(issues)} issues for {review_id}")


if __name__ == "__main__":
    main()
