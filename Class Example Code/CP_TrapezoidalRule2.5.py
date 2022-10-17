#Trapezoidal rule with Dr. Cone
#Example 2.6 from Section 2.5:

#Note: max_[0,1] |f''(x)| need to be claculated/estimated

#For example, consider the integral:
    #I(f) = \int_0^1 * e^{-x^2}
#How small does  it have to be to guarantee that
    #|I(f) - T_n(f)| < 10^-3?"

import math
#Approximates integral of given function f using the Trapezoidal Rule
#On an evenly-spaced grid, where n is is the number of subintervals, lowlim is
#lower limit of integration, and uplim is the upper limit of integration
def Trap1(f, n, lowlim, uplim):
    sum = .5 * (f(lowlim) + f(uplim))

    h = (uplim - lowlim) / n

    for i  in range( 1, n):
        x = lowlim + i*h
        sum = sum + f(x)
    
    return(h*sum)


#Determines error in number of subintervals used for
#given theoretical bound on |f''(x)| (simple) Trapezoidal rule
#used to approximate a given function, within given
#error bound error_bound

#Note, incoming arguments:
#   fdoubleprime_bound - bound for |f''(x)| on [0,1] neeeded
#   lowlim - lower limit of integration (usually denote: a)
#   uplim - upper limit of integration (usually denote: b)
#   errtol - acceptable error tolerance for Trap approx

def ErrorTrap(lowlim, uplim, errtol, fdoubleprime_bound, verbose = False):
    #Arbitrary choice 100 here
    MAX = 100
    for n in range(1, MAX):
        #Slower moves linearly through # of subintervals:
        h = (uplim - lowlim)/n

        #Faster - double the number of subintervals on each estimation:
        #h = (uplim - lowlim) / (2**n)

        err = (uplim - lowlim) / 12.0 * (math.pow*(h,2)) * fdoubleprime_bound

        if(err <= errtol):
            if(verbose):
                print('Approx. within {:8.8f} for {} where h = {:10.8f}' .format(err, n, h)  )
            break
    #Returns guaranteed minimum number of traps needed for given conditions
    return (n)

#Integrand of erf(x):
def Ierf(x):
    return ( math.exp(-1.0*math.pow(x, 2.0)))

a = 0.0
b = 1.0
T4 = Trap1(Ierf, 4, a, b)
T8 = Trap1(Ierf, 8, a, b)
T16 = Trap1(Ierf, 16, a, b)
IR = (4.0*T8 - T4)/3.0