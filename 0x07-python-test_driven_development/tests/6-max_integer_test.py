#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)
    
    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)
    
    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([89]), 89)
    
    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
    
    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 2, 4, 2, 2]), 5)
    
    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 3, 4, 5, 6]), 6)
    
    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 14)
    
    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 3, 7, 5, 1, 6]), 7)
    
    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 3, 4, 5, 6]), 6)
    
    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98, 30, float('nan'), 5, 6]), 98)
    
    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 30, float('inf'), 5, 6]), float('inf'))

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([2, 3, [], "zab", 4, 5, 6])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([2, 3, "zab"])

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{2 : 3, 13 : 14}, {"zab" : "4 5 6"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(100)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(10.0)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, -3, 4, -5, 6, 7, 30]), 30)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, -3, -44, -5, 6, 7, 30, -32,
            22, 3, -40,  5, 60, 71, -78, -49, 10, 11, 12, -113, 104,
            2, -302, -440, -501, 606, 700, 310, -320, 221, 30, -401,
            50, 603, 710, -780, -490, 100, 110, 120, -1130, 1040,
            -1013, 1044, 256, -3021, -4460, -5081, 6069, 7005, 3160,
            -3120, 2201, 3055, -4101, 5101, 6103, 7100, -7890, -4090,
            1010, 1190, 1209, -11300, 10430]), 10430)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2.1, -3.7, 4.8,
            -5.3, 6.7, 7.7, 30.6]), 30.6)

    def test_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2.6, -3.7, -4.4, -5.6, 6.5, 7.3,
            3.0, -3.2, 2.2, 4.3, -4.0,  8.5, 6.0, 7.1, -7.8, -4.9, 1.0,
            1.1, 1.2, -11.3, 10.4, 8.2, -3.02, -44.0, -5.01, 60.6, 70.0
            , 31.0, -32.0, 22.1, 30.4, -401.65, 5.80, 60.3, 710.0, -780.7,
            -49.0, 100.6, 110.7, 12.90, -11.30, 104.0, -101.3, 1040.9,
            256.2, -302.1, -44.60, -508.1, 606.9, 700.5, 316.0, -312.0,
            220.1, 305.5, -410.1, 510.1, 610.3, 710.0, -789.0, -409.0,
            101.0, 119.0, 120.9, -1130.0, 1043.1]), 1043.1)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2.1, -3, 4.8, -5.3, 6, 7, 30]), 30)

    def test_ints_and_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, -3, -44, -5, 6, 7, 30, -32,
            22, 3, -40,  5, 60, 71, -78, -49, 10, 11, 1.2, -11.3, 10.4,
            2, -3.02, -440, -501, 606, 700, 310, -320, 221, 30, -401,
            50, 603, 710, -780, -490, 100, 110, 120, -11.30, 104.0,
            -1013, 1040, 256, -3021, -4460, -5081, 606.9, 700.5, 316.0,
            -312.0, 220.1, 305.5, -4101, 510.1, 610.3, 710.0, -7890,
            -4090, 1010, 119.0, 120.9, -11300, 1043.0]), 1043.0)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-20, -3, -44, -5, -6, -7, -30,
            -32,-22, -3, -40, -15, -60, -71, -78, -49, -10, -11, -12,
            -113, -104, -2, -302, -440, -501, -606, -700, -310, -320,
            -221, -30, -401, -50, -603, -710, -780, -490, -100, -110,
            -120, -1130, -1040, -1013, -1044, -256, -3021, -4460,
            -5081, -6069, -7005, -3160, -3120, -2201, -3055, -4101,
            -5101, -6103, -7100, -7890, -4090, -1010, -1190, -1209,
            -11300, -10430]), -2)


if __name__ == "__main__":
    unittest.main()
