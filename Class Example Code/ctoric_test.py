import sympy
x = sympy.symbols("x")
x0 = sympy.symbols("x0")
ksi = sympy.symbols("ksi")

def deriv(degree, poly, evalVar):
    if(degree >= 0):
        retDeriv = poly
        for i in range(degree):
            retDeriv = sympy.diff(retDeriv, evalVar)   
        return retDeriv
    else:
        print("Please give a degree >= 0")
        return 0
        