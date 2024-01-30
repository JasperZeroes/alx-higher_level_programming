#Unit Testing
import unittest
from math import pi
from trial import area_of_circle

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas of circle when r >= 0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(2.1), pi * 2.1 ** 2)

    def test_values(self):
        #Makes sure a ValueError is raised where necesary
        self.assertRaises(ValueError, area_of_circle, -2)

    def test_types(self):
        #Makes sure a TypeError is raised where necesary
        self.assertRaises(TypeError, area_of_circle, 3+5j)
        self.assertRaises(TypeError, area_of_circle, True)
        self.assertRaises(TypeError, area_of_circle, 'radius')

'''
For Unittest, do not forget to add the line of code below
        if __name == '__main__':
            unittest.main()

so as to enable you run it from the CLI using
        python3 filename.py

else use 
        python3 -m unittest filename.py from CLI directly
'''    
