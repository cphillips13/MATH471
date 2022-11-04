"""
Corey Phillips
Started 11/02/22
Last updated 11/02/22
Stored in MATH471 repo on github.com/cphillips13

Question 3.1.3 Parts B, D, F, H
Write a program that uses the bisection method to find the root of a given
function on a given interval, and apply this program to find the roots of the
functions below on the indicated intervals. Use the relationship 3.2 to 
determine a priori, the number of steps necessary for the root to be accurate
within 10^-6

B: f(x) = e^x - 2, [a,b] = [0,1];
D: f(x) = x^6 - x - 1, [a,b] = [0,2];
F: f(x) = 1 - 2xe^(-x/2), [a,b] = [0,2];
H: f(x) = x^2 - sin(x), [a,b] = [0,pi];

Relationship 3.2:
Let [a0,b0] = [a,b] be the initial interval, with f(a)*f(b) < 0.
Define the apprx root as xn = cn = (bn-1 + an-1)/2
Then there exists a root alpha is in [a,b]
Such that abs(alpha - xn) <= (1/2)^n * (b-a)
To achieve an accuracy of abs(alpha - xn) <= epsilon
take n >= log(b-a) - log(epsilon) / log(2)

Accuracy for this required: 10^-6, this is our epsilon
For B: n >= log(1) - log(10^-6) / log(2)
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def bisectionMethod(upper, lower, equation, priori):
    retval = -999999
    if(equation == 'b' or 'd' or 'f' or 'h'):
        for i in range(priori):
            if(equation == 'b'):
                middle = (upper + lower) / 2
                upperVal = math.e**upper - 2
                lowerVal = math.e**lower - 2
                middleVal = math.e**middle - 2
            elif(equation == 'd'):
                middle = (upper + lower) / 2
                upperVal = upper**6 - upper - 1
                lowerVal = lower**6 - lower - 1
                middleVal = middle**6 - middle - 1
            elif(equation == 'f'):
                middle = (upper + lower) / 2
                upperVal = 1 - 2*upper*math.e**(-upper/2)
                lowerVal = 1 - 2*lower*math.e**(-lower/2)
                middleVal = 1 - 2*middle*math.e**(-middle/2)
            elif(equation == 'h'):
                middle = (upper + lower) / 2
                upperVal = upper**2 - math.sin(upper)
                lowerVal = lower**2 - math.sin(lower)
                middleVal = middle**2 - math.sin(middle)

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

def priori(upper, lower, epsilon):
    retval = math.ceil(math.log(upper-lower) - math.log(epsilon) / math.log(2))
    return retval

def main():
    epsilon = 10**-6

    bUpper = 1
    bLower = 0
    bPriori = priori(bUpper,bLower, epsilon)
    bSol = bisectionMethod(bUpper, bLower, 'b', bPriori)

    dUpper = 2
    dLower = 0
    dPriori = priori(dUpper, dLower, epsilon)
    dSol = bisectionMethod(dUpper, dLower, 'd', dPriori)

    fUpper = 2
    fLower = 0 
    fPriori = priori(fUpper, fLower, epsilon)
    fSol = bisectionMethod(fUpper, fLower, 'f', fPriori)

    hUpper = math.pi
    hLower = 0
    hPriori = priori(hUpper, hLower, epsilon)
    hSol = bisectionMethod(hUpper, hLower, 'h', hPriori)

    print('Problem B: \nf(x) = e^x - 2, [a,b] = [0,1]\nPriori:{}'\
        .format(bPriori))
    print('Problem B Solution: {} \n'.format(bSol))

    print('Problem D: \nf(x) = x^6 - x - 1, [a,b] = [0,2]\nPriori:{}'\
        .format(dPriori))
    print('Problem D Solution: {} \n'.format(dSol))

    print('Problem F: \nf(x) = 1 - 2xe^(-x/2), [a,b] = [0,2]\nPriori:{}'\
        .format(fPriori))
    print('Problem F Solution: {}\n'.format(fSol))

    print('Problem H: \nf(x) = x^2 - sin(x), [a,b] = [0,pi]\nPriori:{}'\
        .format(hPriori))
    print('Problem H Solution: {}\n'.format(hSol))

    X1 = np.arange(0, 1, .05)
    X2 = np.arange(0, 2, .05)
    X3 = np.arange(0, 2, .05)
    X4 = np.arange(0, math.pi, .05)
    Y1 = math.e**X1 - 2
    Y2 = X2**6 - X2 - 1
    Y3 = 1 - 2*X3*math.e**(-X3/2)
    Y4 = X4**2 - np.sin(X4)
    
    figure, axis = plt.subplots(2,2)

    axis[0, 0].plot(X1, Y1)
    axis[0, 0].axvline(bSol)
    axis[0, 0].set_title("f(x) = e^x - 2, [a,b] = [0,1]")
  
    axis[0, 1].plot(X2, Y2)
    axis[0, 1].axvline(dSol)
    axis[0, 1].set_title("f(x) = x^6 - x - 1, [a,b] = [0,2]")
  
    axis[1, 0].plot(X3, Y3)
    axis[1,0].axvline(fSol)
    axis[1, 0].set_title("f(x) = 1 - 2xe^(-x/2), [a,b] = [0,2]")
  
    axis[1, 1].plot(X4, Y4)
    axis[1,1].axvline(hSol)
    axis[1, 1].set_title("f(x) = x^2 - sin(x), [a,b] = [0,pi]")

    plt.subplots_adjust(wspace = .6, hspace = .4)
    plt.show()

main()
