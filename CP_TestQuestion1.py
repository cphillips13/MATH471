# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:14:00 2022

@author: cphil
"""

import math

order = 14
x = 2
center = 1

function = (math.e**x - math.e**(-1*x)) / 2

def evenDerivFunction(x):
    
    return (math.e**x - math.e**(-1*x)) / 2
def oddDerivFunction(x):
    return (math.e**x + math.e**(-1*x))/2

def taylors(x, order, center):
    retval = evenDerivFunction(x)
    if center == 0:
        return retval
    
    for i in range(order):
        if i%2 == 1:
            retval = retval + (oddDerivFunction(center)*((x-center**i))/math.factorial(i))
        elif i%2 == 0:
            retval = retval + (evenDerivFunction(center)*((x-center)**i))/math.factorial(i)
            
    return retval

for i in range(order):
    if(i == 11):
        print("THIS IS WHERE IT REACHES SINGLE PRECISION BELOW")
        print("It reaches single precision accuracy at the 11th order taylor polynomial.")
    print(taylors(x, i, center) - evenDerivFunction(x))
    
