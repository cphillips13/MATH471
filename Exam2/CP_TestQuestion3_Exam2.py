"""
Corey Phillips
Exam 2
11/11/22

Question: 3
"""

import math 
import matplotlib.pyplot as plt
import numpy as np

def priori(upper, lower, epsilon):
    retval = math.ceil((math.log(upper-lower) - math.log(epsilon)) / math.log(2))
    return retval

def fx(x):
    return (x**(x**x)) - 3.5

def bisectionMethod(upper, lower, priori):
    retval = -999999
    for i in range(priori):
        middle = (upper + lower) / 2
        upperVal = fx(upper)
        lowerVal = fx(lower)
        middleVal = fx(middle)

        if(middleVal == 0):
            retval = middle
        elif(upperVal == 0):
            retval = upper
        elif(lowerVal == 0):
            retval = lower
        elif(lowerVal > 0 and middleVal > 0 or lowerVal < 0 and middleVal < 0):
            lower = middle
            retval = lower
        elif(upperVal > 0 and middleVal > 0 or upperVal < 0 and middleVal < 0):
            upper = middle
            retval = upper
    return retval

def regulaFalsi(upper, lower, epsilon):
    retval = 1
    error = 1
    count = 1
    while(error > epsilon):
        prev = retval
        upperVal = fx(upper)
        lowerVal = fx(lower)
        if(upperVal == 0):
            retval = upper
        elif(lowerVal == 0):
            retval = lower
        else:
            lower = upper - upperVal*(upper-lower) / (upperVal - lowerVal)
            retval = lower
        error = retval - prev
        count = count + 1
    return count

def fprime(x):
    return x**x**x

def newton(x0, epsilon):
    retval = x0 - (fx(x0)/fprime(x0))
    error = 1
    count = 1
    while(error > epsilon):
        oldRetval = retval
        retval = retval - (fx(retval)/fprime(retval))
        error = oldRetval - retval
        count = count + 1

    print(count)
    return retval

def main():

    epsilon = 10**(-6)
    aLower = 1
    aUpper = 2
    aPriori = priori(aUpper, aLower, epsilon)
    aSol = bisectionMethod(aUpper, aLower, aPriori)
    aSolRegulaFalsi = regulaFalsi(aUpper, aLower, epsilon)

    print('Problem A: \na: f(x) = x^x^x - 3.5, [a, b] = [1,2]\nBisection:{}\nRegulaFalsi: {}'\
        .format(aPriori, aSolRegulaFalsi))
    print('Problem A Solution: {} \n'.format(aSol))

    x0 = 1
    print("Newtons: {}".format(newton(x0, epsilon)))

main()