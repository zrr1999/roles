"""Tests for commit_message_validator."""

from __future__ import annotations

import unittest

from tools.hooks.commit_message_validator import validate_commit_message


class TestValidateCommitMessage(unittest.TestCase):
    def test_valid_with_emoji(self) -> None:
        self.assertIsNone(validate_commit_message("✨ feat: add more functionality\n"))

    def test_valid_with_scope_and_bang(self) -> None:
        self.assertIsNone(validate_commit_message("🔧 fix(api)!: handle edge case"))

    def test_merge_allowed(self) -> None:
        self.assertIsNone(validate_commit_message("Merge branch 'main' into foo"))

    def test_revert_allowed(self) -> None:
        self.assertIsNone(validate_commit_message("Revert \"something\""))

    def test_fixup_allowed(self) -> None:
        self.assertIsNone(validate_commit_message("fixup! ✨ feat: prior"))

    def test_empty_fails(self) -> None:
        err = validate_commit_message("")
        self.assertIsNotNone(err)
        self.assertIn("non-empty summary", err or "")

    def test_comment_only_fails(self) -> None:
        err = validate_commit_message("# comment\n")
        self.assertIsNotNone(err)

    def test_missing_emoji_fails(self) -> None:
        err = validate_commit_message("feat: no emoji prefix\n")
        self.assertIsNotNone(err)

    def test_invalid_type_fails(self) -> None:
        err = validate_commit_message("✨ foo: bar\n")
        self.assertIsNotNone(err)


if __name__ == "__main__":
    unittest.main()
