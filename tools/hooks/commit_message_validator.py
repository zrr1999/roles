"""Repository-local commit message validation for git hook integration."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ALLOWED_TYPES = (
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
)
SPECIAL_PREFIXES = ("Merge ", "Revert ", "fixup! ", "squash! ")
COMMIT_PATTERN = re.compile(rf"^\S+\s+({'|'.join(ALLOWED_TYPES)})(\([^)]+\))?(!)?:\s+\S.*$")
EXAMPLE_MESSAGE = "✨ feat: add more functionality"


def first_summary_line(message: str) -> str:
    """Return the first meaningful summary line from a commit message."""
    for line in message.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped
    return ""


def validate_commit_message(message: str) -> str | None:
    """Return an error string when the message is invalid."""
    summary = first_summary_line(message)
    if not summary:
        return f"Commit message must include a non-empty summary line. Expected format: {EXAMPLE_MESSAGE}"

    if summary.startswith(SPECIAL_PREFIXES):
        return None

    if COMMIT_PATTERN.match(summary):
        return None

    allowed_types = ", ".join(ALLOWED_TYPES)
    return (
        "Commit message must match '<emoji> <type>(<scope>)?: <subject>' "
        f"using one of: {allowed_types}. Example: {EXAMPLE_MESSAGE}"
    )


def main(argv: list[str] | None = None) -> int:
    """Validate the commit message file passed by git's commit-msg hook."""
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("Usage: python -m tools.hooks.commit_message_validator <commit-msg-file>", file=sys.stderr)
        return 2

    commit_message_path = Path(args[0])
    message = commit_message_path.read_text(encoding="utf-8")
    error = validate_commit_message(message)
    if error is None:
        return 0

    print(error, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
