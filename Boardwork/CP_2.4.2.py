#Corey Phillips:
#Started 10/19

#The gamma function denoted by GAMMA(x) occurs in a number of applications
#Most notably probability theory and the solution of certain differential equations
#It is basically the generalization of the factorial function to non-integer values, in that
#GAMMA(n + 1) = n!
#Table 2.8 gives values of GAMMA(x) for x between 1 and 2. Use linear interpolation to
#approximate values of GAMMA(x) as given below

#Approximate these values:
#GAMMA(1.930) = .9723969178
#GAMMA(1.290) = .8990415863
#GAMMA(1.005) = .9971385354
#GAMMA(1.635) = .8979334930

#Table of GAMMA(x) values:
#x            |GAMMA(x)
#1.00         |1.0
#1.10         |0.9513507699
#1.20         |0.9181687424
#1.30         |0.8974706963
#1.40         |0.8872638175
#1.50         |0.8862269255
#1.60         |0.8935153493
#1.70         |0.9086387329
#1.80         |0.9313837710       
#1.90         |0.9617658319
#2.00         |1.0

import math
import numpy as np

#First lets set some variables:
tableX = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
tableGX = [1.0, 0.9513507699, 0.9181687424, 0.8974706963, 0.8872638175, 0.8862269255, 0.8935153493, 0.9086387329, 0.9313837710, 0.9617658319, 1.0]

table = np.array(tableX, tableGX)

x = [1.29, 1.579, 1.456, 1.314, 1.713]

def truncate(x, digits):
    nbDecimal = len(str(x).split('.')[1])
    if nbDecimal <= digits:
        return x
    return math.trunc(10**digits * x) / (10**digits)

def p1(x):
    retval = 0
    low = truncate(x, 1)
    high = low+.1

    #((x - low)/(high-low)) 
    return retval
p1(x[1])

print(table[0][0])
