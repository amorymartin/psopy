# -*- coding: utf-8 -*-


"""
python3 -m tests.test_advanced
"""

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
