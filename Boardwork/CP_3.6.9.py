"""
Write a program using Newton's method to find the root of:
f(x) = 1 - e^(-x^2)

The exact value is alpha = 0. Compute the ratio:

Rn = alpha - Xn+1   /  (alpha - Xn)^2



"""
import math
import numpy as np
import matplotlib.pyplot as plt
alpha = 0

#At a base level, this problem does not
#Work the way we expect at zero.
#It does not pass one of the conditions of Newtons method
#because f'(alpha) = 0. 

def gx(x):
    return (1 - math.e**(-x**2))

def fx(x):
    return (-1 - math.e**(-x**2))

#Cool things I have noticed:
#Playing with scaling by adding or subracting to 
#The original function does some cool things
#As we scale it past 1, the value that we return from 
#Rn is 1/(amount we scaled up + 1)


def priori(upper, lower, epsilon):
    retval = abs(math.ceil((math.log(upper-lower) - math.log(epsilon)) / math.log(2)))
    return retval

def bisectionMethod(upper, lower, priori):
    retval = -999999
    for i in range(priori):
        middle = (upper + lower) / 2
        upperVal = gx(upper)
        lowerVal = gx(lower)
        middleVal = gx(middle)

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

epsilon = 10**(6)
aLower = -1
aUpper = 1
aPriori = priori(aUpper, aLower, epsilon)
print(aPriori)
aSol = bisectionMethod(aUpper, aLower, aPriori)

print('Problem A: \na: f(x) = 1 - math.e**(-x**2)), [a, b] = [-1,1]\nBisection:{}'\
    .format(aSol))

X1 = np.arange(-2, 2, .05)
X2 = np.arange(-2, 2, .05)
X3 = np.arange(-2, 2, .05)
X4 = np.arange(-2,-.0001, .05)
Y1 = fx(X1)
Y2 = alpha - fx(X2+1)
Y3 = (alpha - fx(X3))**2
Y4 = (alpha - fx(X4+1))/((alpha - fx(X4))**2)
    
figure, axis = plt.subplots(2,2)

axis[0, 0].plot(X1, Y1)
axis[0,0].axhline(0)
axis[0, 0].set_title("1-math.e**(-X1**2)")
  
axis[0, 1].plot(X2, Y2)
axis[0, 1].axhline(0)
axis[0, 1].set_title("f(x) = x^6 - x - 1, [a,b] = [0,2]")
  
axis[1, 0].plot(X3, Y3)
axis[1,0].axhline(0)
axis[1, 0].set_title("f(x) = 1 - 2xe^(-x/2), [a,b] = [0,2]")
  
axis[1, 1].plot(X4, Y4)
axis[1,1].axhline(0)
axis[1, 1].set_title("f(x) = x^2 - sin(x), [a,b] = [0,pi]")

for i in range(10):
    print((alpha - fx(i+1) )/((alpha - fx(i))**2))

plt.subplots_adjust(wspace = 1, hspace = 1)
plt.show()