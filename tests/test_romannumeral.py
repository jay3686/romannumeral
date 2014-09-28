#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_romannumeral
----------------------------------

Tests for `romannumeral` module.
"""

import unittest

from romannumeral import RomanNumeral

from romannumeral import ParseError
from romannumeral import OutOfRangeError


class TestRomannumeral(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_roman_from_int(self):
        r = RomanNumeral(10)

        assert r.value == 10
        assert r.string == 'X'

    def test_create_roman_from_str(self):
        r = RomanNumeral('X')

        assert r.value == 10
        assert r.string == 'X'

    def test_create_roman_exhaustive(self):

        for n in xrange(10000):
            if n == 0 or n >= 4000:
                self.assertRaises(OutOfRangeError, RomanNumeral, n)
            else:
                r = RomanNumeral(n)
                assert r.value == n

    def test_roman_from_badstring(self):
        """ Roman from malformed string should through parse exception """
        pass

    def test_roman_from_decimal(self):
        """ Roman from malformed string should through parse exception """
        self.assertRaises(ParseError, RomanNumeral, 3.14)

    def test_roman_from_negative(self):
        """ Roman below 0 throw an overflow exception """
        self.assertRaises(OutOfRangeError, RomanNumeral, -1)


    def test_roman_from_over_3999(self):
        """ Roman over 3999 throw an overflow exception """
        self.assertRaises(OutOfRangeError, RomanNumeral, 9001)


if __name__ == '__main__':
    unittest.main()
