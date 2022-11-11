"""
a: f(x) = x - e^(-x^2), [a, b] = [0,1]
b: f(x) = lnx + x, [a, b] = [1/10, 1]
c: f(x) = x^3 - 3, [a, b] = [0,3]
d: f(x) = x^6 - x - 1 [a, b] = [0,2]
e: f(x) = 3 - 2^x, [a, b] = [0, 2]

To find priori: 

def priori(upper, lower, epsilon):
    retval = math.ceil((math.log(upper-lower) - math.log(epsilon)) / math.log(2))
    return retval

"""

import math 
import matplotlib.pyplot as plt
import numpy as np

def priori(upper, lower, epsilon):
    retval = math.ceil((math.log(upper-lower) - math.log(epsilon)) / math.log(2))
    return retval

def bisectionMethod(upper, lower, equation, priori):
    retval = -999999
    if(equation == 'a' or 'b' or 'c' or 'd' or 'e'):
        for i in range(priori):
            if(equation == 'a'):
                middle = (upper + lower) / 2
                upperVal = upper - math.e**(-1*upper**2)
                lowerVal = lower - math.e**(-1*lower**2)
                middleVal = middle - math.e**(-1*middle**2)
            elif(equation == 'b'):
                middle = (upper + lower) / 2
                upperVal = math.log(upper) + upper
                lowerVal = math.log(lower) + lower
                middleVal = math.log(middle) + middle
            elif(equation == 'c'):
                middle = (upper + lower) / 2
                upperVal = upper**3 - 3
                lowerVal = lower**3 - 3
                middleVal = middle**3 - 3
            elif(equation == 'd'):
                middle = (upper + lower) / 2
                upperVal = upper**6 - upper - 1
                lowerVal = lower**6 - lower - 1
                middleVal = middle**6 - middle - 1
            elif(equation == 'e'):
                middle = (upper + lower) / 2
                upperVal = 3 - 2**upper
                lowerVal = 3 - 2**lower
                middleVal = 3 - 2**middle

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

def regulaFalsi(upper, lower, priori):
    retval = -999999
    for i in range(priori):
        upperVal = upper**3 - 2
        lowerVal = lower**3 - 2
        if(upperVal == 0):
            retval = upper
        elif(lowerVal == 0):
            retval = lower
        else:
            lower = upper - upperVal*(upper-lower) / (upperVal - lowerVal)
            retval = lower
        print(retval)
    return retval

def main():

    epsilon = .00000000000001

    aLower = 0
    aUpper = 1
    aPriori = priori(aUpper, aLower, epsilon)
    aSol = bisectionMethod(aUpper, aLower, 'a', aPriori)
    aSolRegulaFalsi = regulaFalsi(2, 0, 3)
    print("Here is the regulaFalsi for a: {}".format(aSolRegulaFalsi))

    bLower = 1/10
    bUpper = 1
    bPriori = priori(bUpper, bLower, epsilon)
    bSol = bisectionMethod(bUpper, bLower, 'b', bPriori)

    cLower = 0
    cUpper = 3
    cPriori = priori(cUpper, cLower, epsilon)
    cSol = bisectionMethod(cUpper, cLower, 'c', cPriori)

    dLower = 0
    dUpper = 2
    dPriori = priori(dUpper, dLower, epsilon)
    dSol = bisectionMethod(dUpper, dLower, 'd', dPriori)

    eLower = 0
    eUpper = 2
    ePriori = priori(eUpper, eLower, epsilon)
    eSol = bisectionMethod(eUpper, eLower, 'e', ePriori)

    print('Problem A: \na: f(x) = x - e^(-x^2), [a, b] = [0,1]\nPriori:{}'\
        .format(aPriori))
    print('Problem A Solution: {} \n'.format(aSol))

    print('Problem B: \nb: f(x) = lnx + x, [a, b] = [1/10, 1]\nPriori:{}'\
        .format(bPriori))
    print('Problem B Solution: {} \n'.format(bSol))

    print('Problem C: \nc: f(x) = x^3 - 3, [a, b] = [0,3]\nPriori:{}'\
        .format(cPriori))
    print('Problem C Solution: {}\n'.format(cSol))

    print('Problem D: \nd: f(x) = x^6 - x - 1 [a, b] = [0,2]\nPriori:{}'\
        .format(dPriori))
    print('Problem D Solution: {}\n'.format(dSol))

    print('Problem E: \ne: f(x) = 3 - 2^x, [a, b] = [0, 2]\nPriori:{}'\
        .format(ePriori))
    print('Problem E Solution: {}\n'.format(eSol))
"""
    X1 = np.arange(0, 1, .05)
    X2 = np.arange(1/10, 1, .05)
    X3 = np.arange(0, 3, .05)
    X4 = np.arange(0, 2, .05)
    Y1 = X1 - math.e**(-X1**2)
    Y2 = np.log(X2) + X2
    Y3 = X3**3 - 3
    Y4 = X4**6 - X4 - 1
    
    figure, axis = plt.subplots(2,2)

    axis[0, 0].plot(X1, Y1)
    axis[0, 0].axvline(aSol)
    axis[0,0].axhline(0)
    axis[0, 0].set_title("f(x) = x - e^(-x^2), [a, b] = [0,1]")
  
    axis[0, 1].plot(X2, Y2)
    axis[0, 1].axvline(bSol)
    axis[0, 1].axhline(0)
    axis[0, 1].set_title("f(x) = lnx + x, [a, b] = [1/10, 1]")
  
    axis[1, 0].plot(X3, Y3)
    axis[1,0].axvline(cSol)
    axis[1,0].axhline(0)
    axis[1, 0].set_title("f(x) = x^3 - 3, [a, b] = [0,3]")
  
    axis[1, 1].plot(X4, Y4)
    axis[1,1].axvline(dSol)
    axis[1,1].axhline(0)
    axis[1, 1].set_title("f(x) = x^6 - x - 1 [a, b] = [0,2]")


    plt.subplots_adjust(wspace = .6, hspace = .4)
    plt.show()
"""
main()
