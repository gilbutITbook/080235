#!/usr/bin/env python3.8
from unittest import TestCase, main
from utils import to_str

class AssertTestCase(TestCase):
    def test_assert_helper(self):
        expected = 12
        found = 2 * 5
        self.assertEqual(expected, found)

    def test_assert_statement(self):
        expected = 12
        found = 2 * 5
        assert expected == found


if __name__ == '__main__':
    main()
