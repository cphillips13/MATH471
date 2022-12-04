#Here is where I will be putting my blank bisection method
#The idea is to be able to put this bisection method into any program and expect it to work.

#Bisection splits a range of a function in two then keeps going until it finds the root of the function.

#How does bisection work? 
#Bisection works by being given a function as well as a range to test roots on.
#This range is your [x0,x1] you will either be given this or have to take an educated guess. 

#Input your function or functions into here:
fx = lambda x: x**2 - 3

#Ex how to use lambda:       print(fx(2))

def bisection(x0, x1, priori):
    retval = False

    middle = (x0 + x1)/2

    for i in range(priori):
        if(fx(middle) == 0):
            retval = middle
            break
        elif(fx(x0) == 0):
            retval = x0
            break 
        elif(fx(x1) == 0):
            retval = x1
            break 

        if(fx(x0) < 0 and fx(middle) > 0 or fx(x0) > 0 and fx(middle) < 0):
            x1 = middle

    return retval