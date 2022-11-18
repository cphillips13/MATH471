"""
Corey Phillips
Exam 2
11/11/22

Question: 2
"""

import math

def ax(x):
    return (math.e**x - math.e**(-x)) / 2

def bx(x):
    return (math.sqrt(1-x**4))

def trapBasic(upper, lower,size, func):
    interval = (upper - lower) / size
    nextBlock = lower + interval
    retval = 0
    if(func == 'a'):
        sum = ax(lower) + ax(upper)
        for i in range(size-1):
            sum = 2*ax(nextBlock) + sum
            nextBlock = nextBlock + interval
        retval = interval / 2 * (sum)
    elif(func == 'b'):
        sum = bx(lower) + bx(upper)
        for i in range(size-1):
            sum = 2*bx(nextBlock) + sum
            nextBlock = nextBlock + interval
        retval = interval / 2 * (sum)
    return retval

def main():
    upper = 2
    lower = 0
    size = 2

    print("Problem A:")
    print("Size: {} Tnf: {}".format(size, trapBasic(upper, lower, size, 'a')))

    for i in range(6):
        size = size*2
        print("Size: {} Tnf: {}".format(size, trapBasic(upper, lower, size, 'a')))
    
    upper = 1
    lower = -1
    size = 2
    print("Problem B:")
    print("Size: {} Tnf: {}".format(size, trapBasic(upper, lower, size, 'b')))

    for i in range(6):
        size = size*2
        print("Size: {} Tnf: {}".format(size, trapBasic(upper, lower, size, 'b')))
    
    return 0

main()
