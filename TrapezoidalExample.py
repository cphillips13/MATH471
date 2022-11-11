import math

def fx(x):
    return math.e**x


def trap(grid, upper, lower):
    retval = 0
    subinterval = (upper - lower) / grid
    for i in range(int(subinterval)):
        retval = fx(lower + grid*i) + retval
    retval = grid*subinterval*retval
    return retval

def trapError(trap):
    return 0

def main():
    upper = 1
    lower = 0
    grid = .5
    subinterval = (upper - lower) / grid

    print(trap(grid, upper, lower))

    return 0

main()