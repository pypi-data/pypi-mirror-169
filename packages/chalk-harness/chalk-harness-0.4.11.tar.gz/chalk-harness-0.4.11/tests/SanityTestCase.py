import unittest

from chalkharness.chalkharness import ChalkCLIHarness


class SanityTestCase(unittest.TestCase):
    def test_apply(self):
        harness = ChalkCLIHarness(dry=True)
        self.assertEqual(
            ["chalk", "apply", "--json", "--await", "--force"],
            harness.apply_await(True),
        )

    def test_version(self):
        harness = ChalkCLIHarness(dry=True)
        self.assertEqual(
            ["chalk", "version", "--json"],
            harness.version(),
        )
        self.assertEqual(
            ["chalk", "version", "--json", "--tag-only"],
            harness.version_tag_only(),
        )

    def test_whoami(self):
        harness = ChalkCLIHarness(dry=True)
        self.assertEqual(
            ["chalk", "whoami", "--json"],
            harness.whoami(),
        )

    def test_token(self):
        harness = ChalkCLIHarness(dry=True)
        self.assertEqual(
            ["chalk", "token", "--json"],
            harness.token(),
        )


if __name__ == "__main__":
    unittest.main()
