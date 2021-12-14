# https://docs.python.org/3/library/unittest.html
import unittest
from areacircle import area_of_circle
from math import pi

class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        # Test radius >=0
        self.assertAlmostEqual(area_of_circle(1),pi)
        self.assertAlmostEqual(area_of_circle(0),0)
        self.assertAlmostEqual(area_of_circle(3.5),pi*3.5**2)
    def test_values(self):
        # Test that bad values are caught
        self.assertRaises(ValueError, area_of_circle, -1)

if __name__ == '__main__':
    unittest.main()

# output:.F
# ======================================================================
# FAIL: test_values (__main__.Test_Area_of_Circle_input)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "e:/OneDrive/10 Project/00.001_Python_snippets/01_unittest/02_test_area_and_value.py", line 13, in test_values
#     self.assertRaises(ValueError, area_of_circle, -1)
# AssertionError: ValueError not raised by area_of_circle        

# -----------------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1)