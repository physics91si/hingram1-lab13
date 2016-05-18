#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc('1+1'), 2)

    def testSubtraction(self):
        self.assertEqual(calc.calc('1-1'), 0)

    def testMultiplication(self):
        self.assertEqual(calc.calc('6*3'), 18) 
 
    def testDivision(self):
        self.assertEqual(calc.calc('6/2'), 3)

if __name__ == '__main__':
    unittest.main()

