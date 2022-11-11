import math

def fx(x):
    return (x - math.e**(-x**2))

def fprime(x):
    return (2*x*math.e**(-x**2) +1)

def newton(x0, epsilon):
    retval = x0 - (fx(x0)/fprime(x0))
    error = 1
    count = 1
    while(error > epsilon):
        oldRetval = retval
        retval = retval - (fx(retval)/fprime(retval))
        error = abs(oldRetval - retval)
        count = count + 1
    print(count)
    return retval

def main():
    x0 = 0
    epsilon = .00000000000001

    print(newton(x0, epsilon))

main()