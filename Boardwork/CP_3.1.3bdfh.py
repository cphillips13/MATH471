"""
Corey Phillips
Started 11/02/22
Last updated 11/02/22
Stored in MATH471 repo on github.com/cphillips13

Question 3.1.3 Parts B, D, F, H
Write a program that uses the bisection method to ifnd the root of a given
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

def priori(upper, lower, epsilon):
    retval = math.ceil(math.log(upper-lower) - math.log(epsilon) / math.log(2))
    return retval

def main():
    epsilon = 10**-6
    bUpper = 1
    bLower = 0

    dUpper = 2
    dLower = 0

    fUpper = 2
    fLower = 0 

    hUpper = math.pi
    hLower = 0

    print('Problem B: \nf(x) = e^x - 2, [a,b] = [0,1]\nPriori:{}'\
        .format(priori(bUpper,bLower,epsilon)))
    print('Problem D: \nf(x) = x^6 - x - 1, [a,b] = [0,2]\nPriori:{}'\
        .format(priori(dUpper,dLower,epsilon)))
    print('Problem F: \nf(x) = 1 - 2xe^(-x/2), [a,b] = [0,2]\nPriori:{}'\
        .format(priori(fUpper,fLower,epsilon)))
    print('Problem H: \nf(x) = x^2 - sin(x), [a,b] = [0,pi]\nPriori:{}'\
        .format(priori(hUpper,hLower,epsilon)))

main()
