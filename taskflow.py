"""Minimal task CLI used as a Git collaboration exercise."""

import argparse
import json
from pathlib import Path

DEFAULT_DB = Path("tasks.json")


def load_tasks(db_path: Path) -> list[dict]:
    if not db_path.exists():
        return []
    return json.loads(db_path.read_text(encoding="utf-8"))


def save_tasks(db_path: Path, tasks: list[dict]) -> None:
    db_path.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A tiny task manager")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_subparsers(dest="command", required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    raise SystemExit(f"unsupported command: {args.command}")


if __name__ == "__main__":
    main()
