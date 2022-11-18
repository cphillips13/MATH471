import math

def fx(x):
    return math.e**(-x**2)


def trapBasic(upper, lower,size):
    interval = (upper - lower) / size
    nextBlock = lower + interval
    retval = 0
    sum = fx(lower) + fx(upper)
    for i in range(size-1):
        sum = 2*fx(nextBlock) + sum
        nextBlock = nextBlock + interval
    retval = interval / 2 * (sum)
    return retval
"""
1/12h^2 |f''(ksi)| <= 1/12h^2 max|f''(x)|
"""
def trapError(upper, lower, h):
    
    return 0

def main():
    upper = 2
    lower = 1
    size = 8
    target = 0.1352572580
    epsilon = 10**-3
    print("Size: {} Tnf: {} If - Tnf: {}".format(size, trapBasic(upper, lower, size), target-trapBasic(upper,lower,size)))

    for i in range(10):
        size = size*2
        print("Size: {} Tnf: {} If - Tnf: {}".format(size, trapBasic(upper, lower, size), target-trapBasic(upper,lower,size)))
    
    """
    b-a / 12 * h^2 max|f''(x)| = error
    """


    """
    while(target - trapBasic(upper,lower,size)> epsilon):
        size = size + 1
        print(trapBasic(upper,lower,size))
    h = 1/size

    print(h)
    """
    return 0

main()