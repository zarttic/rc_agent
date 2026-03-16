import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr")
    parser.add_argument("--mr")
    args = parser.parse_args()

    target = args.pr or args.mr
    print(f"Posting comments for {target} (stub)")


if __name__ == "__main__":
    main()
