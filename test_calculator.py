#https://github.com/louizaj/lab10-LJ-JP.git
#Partner 1: Louiza Joya
#Partner 2: Joseph Patriarca

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,-2), -3)
        self.assertEqual(add(10,-2), 8)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,6), -5)
        self.assertEqual(subtract(-2,-4), 2)
        self.assertEqual(subtract(10,3), 7)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-1, -3), 3)
        self.assertEqual(mul(0,-5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,6), 2)
        self.assertEqual(div(-2, 4), -2)
        self.assertEqual(div(2, -6), -3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
         with self.assertRaises(ZeroDivisionError):
            div(0,60)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,100), 2)
        self.assertEqual(logarithm(3,27), 3)
        self.assertEqual(logarithm(25,25), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-10,100)

    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(5,0), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()