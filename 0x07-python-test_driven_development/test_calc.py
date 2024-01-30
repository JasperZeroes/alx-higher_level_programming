#Unit Testing
import unittest
from calc import add, subtract, multiply, divide

class TestCalc(unittest.TestCase):
    def test_calculator(self):
        #tests the functions when x and y are integer or float
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2, -5), -3)
        self.assertEqual(subtract(0,0), 0)
        self.assertEqual(subtract(2,-5), 7)
        self.assertEqual(multiply(0,0), 0)
        self.assertEqual(multiply(2,-5), -10)
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(-5, 2), -2.5)
        

    def test_types(self):
        #tests the functions when x or y are not int or float
        self.assertRaises(TypeError, divide, 2, 'k')
        self.assertRaises(TypeError, multiply,2, 'gh')
        self.assertRaises(TypeError, subtract,'h', 4)
        self.assertRaises(TypeError, add, 2, 'ad')

    def test_zero(self):
        #tests the functions when y == 0
        self.assertRaises(ZeroDivisionError, divide, 3, 0 )
        
'''
For Unittest, do not forget to add the line of code be;ow
so as to enable you run it from the CLI using
    python3 filename.py

if __name == '__main__':
    unittest.main()

else; use python3 -m unittest filename.py from CLI directly
'''    
