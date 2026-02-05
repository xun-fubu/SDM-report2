#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

        # --- ここから同値分割で追加したテスト ---

        def test_equiv_normal_min (self):
                self.assertEqual(1, calc(1,1))

        def test_equiv_negative_x (self):
                self.assertEqual(-1, calc(-3,5))

        def test_equiv_negative_y (self):
                self.assertEqual(-1, calc(2,-7))

        def test_equiv_float (self):
                self.assertEqual(-1, calc(1.0,5))