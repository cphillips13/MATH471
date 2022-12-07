
x0 = 1.5
runtime = 5

def func(x):
    return (x**3)-(2*x)-5

def deriv(x):
    return 3*(x**2) - 2

def newtons(x0, runTime):
    xList = [x0]
    for i in range(runTime):
        xList.append(xList[i] - (func(xList[i])/deriv(xList[i])))

    return xList

tester = newtons(x0,runtime)

print(tester)