# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:30:31 2022

@author: cphil
"""

#Corey Phillips
#Python question number 2

#Class Horners Rule
#incvec: Incoming polynomial, polynomial is input from coefficients x^0 up. 
#This includes using 0x^0 for the operators inbetween.
#Val is the value that we are evaluating this polynomial at
def HornersRuleNaive(incvec, val):
    #retval is the variable we add our horners evaluated polynomial to
    retval = 0.0
    #iterator holds our exponent of the x we are currently at in the array.
    iterator = 0
    for i in incvec:
        retval = (i)*(val**iterator) + retval
        iterator = iterator+1
    return retval

#poly1 = x^13 + 13
poly1 = [13, 0, 0, 0, 0 , 0, 0 , 0, 0, 0, 0, 0, 0, 1]
#derivPoly1 = 13x^12
derivPoly1 = [0, 0, 0, 0 , 0, 0 , 0, 0, 0, 0, 0, 0, 13]
#poly2 = x^5 - 2x^4 + 3x^3 - 4x^2 + 5x - 6
poly2 = [-6, 5, -4, 3, -2 , 1]
#derivPoly2 = 5x^4 - 8x^3 + 9x^2 - 8x + 5
derivPoly2 = [5, -8, 9, -8 , 5]
#poly3 = 1 + x^1 + x^2 + x^3 + x^4 +x^5 + x^6 + x^7 + x^8 +x^9 + x^10
poly3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#derivPoly3 = 1 + 2x + 3x^2 + 4x^3 + 5x^4 + 6x^5 + 7x^6 + 8x^7 + 9x^8 + 10x^9
derivPoly3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#x0 is what we will be evaluating this polynomial at.
x0 = 1

tester = HornersRuleNaive(poly1,x0)
print("poly1 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(poly1,x0)
print("poly1 evaluated at ", x0, " is ", tester)

x0 = 1
tester = HornersRuleNaive(poly2,x0)
print("poly2 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(poly2,x0)
print("poly2 evaluated at ", x0, " is ", tester)

x0 = 1
tester = HornersRuleNaive(poly3,x0)
print("poly3 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(poly3,x0)
print("poly3 evaluated at ", x0, " is ", tester)

x0 = 1
tester = HornersRuleNaive(derivPoly1, x0)
print("derivPoly1 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(derivPoly1, x0)
print("derivPoly1 evaluated at ", x0, " is ", tester)

x0 = 1
tester = HornersRuleNaive(derivPoly2, x0)
print("derivPoly2 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(derivPoly2, x0)
print("derivPoly2 evaluated at ", x0, " is ", tester)

x0 = 1
tester = HornersRuleNaive(derivPoly3, x0)
print("derivPoly3 evaluated at ", x0, " is ", tester)

x0 = 2
tester = HornersRuleNaive(derivPoly3, x0)
print("derivPoly3 evaluated at ", x0, " is ", tester)

