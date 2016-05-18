#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys
import string 
def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print (calc(calculation))

def calc(s):
    """Parse a string describing an operation on quantities with units."""

    # TODO make this robust for differently formatted inputs
    newString = s.replace("\\s+","")
    operand = 
    num1 = s[0]
    num2 = s[2]
    operation = s[1]

    if operation=='+':
        return float(num1)+float(num2)
    elif operation=='-':
        return float(num1)-float(num2)
    elif operation=='*':
        return float(num1)*float(num2)
    elif operation=='/':
        return float(num1)/float(num2)


if __name__ == "__main__": main()
