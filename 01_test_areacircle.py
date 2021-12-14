# Chris Jackson; Jason Gooley; Adrian Iliesiu;Ashutosh Malegaonkar. 
# Cisco Certified DevNet Associate DEVASC 200-901 Official Cert Guide 
 
import unittest 
from areacircle import area_of_circle
from math import pi

class Test_area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        # Test radius >=0
        self.assertAlmostEqual(area_of_circle(1),pi)
        self.assertAlmostEqual(area_of_circle(0),0)
        self.assertAlmostEqual(area_of_circle(3.5),pi*3.5**2)

        
if __name__ == '__main__':
    unittest.main()
# if without this "if block", run following:
# >>>python -m unittest test_areacircle.py

# outputs as follow  
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK


