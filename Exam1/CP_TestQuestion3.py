# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:59:29 2022

@author: cphil
"""

#Corey Phillips
#Test Question 3
#Taylors theorem to approximate the derivative:
    
#%%
import math

#Evaluates the two derivate approximations at x0 and h:
x0 = math.pi / 4
h = 2**(-6)

#Function to evaluate at the taylors derivative formula 
#x0 is what we are plugging in for x
#h is what we are plugging in for h
#switch determines which function is being run
def taylorsDeriv(x0, h, switch):
    retval = (8*partABC(x0 + h, switch) - 8*partABC(x0 - h, switch) - partABC(x0 + 2*h, switch) + partABC(x0 - 2*h, switch))/12
    return retval

#Function to evaluate at the calculus derivative formula 
#x0 is what we are plugging in for x
#h is what we are plugging in for h
#switch determines which function is being run
def calc1Deriv(x0, h, switch):
    retval = (partABC(x0+h, switch) - partABC(x0, switch))/h
    return retval

#Function to determine which of our given functions will be run
#switch 1: function a
#switch 2: function b
#switch 3: function c

def partABC(x0, switch):
    if(switch == 1):
        #function a
        retval = math.cos(2*x0) * 10
        return retval
    elif(switch == 2):
        #function b
        retval = (math.e**x0 - math.e**(-1*x0)) / 2
        return retval
    elif(switch == 3):
        #function c
        retval = x0**x0 
        return retval
    
#What I am storing my values in, I realize now I should have skipped this
#and just included in the print statement instead.
#taylorsDerivApprox holds our taylors deriv at the given parameters
#calc1DerivApprox holds our calc1 deriv at the given parameters
taylorsDerivApprox = 0
calc1DerivApprox = 0

print("Part A using taylors approx: ")
taylorsDerivApprox = taylorsDeriv(x0, h, 1)
print(taylorsDerivApprox)
calc1DerivApprox = calc1Deriv(x0, h, 1)
print("Part A using calc1 approx: ")
print(calc1DerivApprox)
print("Absolute Error between the two: ")
print(abs(taylorsDerivApprox - calc1DerivApprox))

print("Part B using taylors approx: ")
taylorsDerivApprox = taylorsDeriv(x0, h, 2)
print(taylorsDerivApprox)
calc1DerivApprox = calc1Deriv(x0, h, 2)
print("Part B using calc1 approx: ")
print(calc1DerivApprox)
print("Absolute Error between the two: ")
print(abs(taylorsDerivApprox - calc1DerivApprox))

print("Part C using taylors approx: ")
taylorsDerivApprox = taylorsDeriv(x0, h, 2)
print(taylorsDerivApprox)
calc1DerivApprox = calc1Deriv(x0, h, 2)
print("Part C using calc1 approx: ")
print(calc1DerivApprox)
print("Absolute Error between the two: ")
print(abs(taylorsDerivApprox - calc1DerivApprox))
