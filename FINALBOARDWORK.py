import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

"""
fig = plt.figure()

l, = plt.plot([], [], 'k-')

plt.xlim(-5,5)
plt.ylim(-5,5)

def func(x):
    return np.sin(x)*3

xlist = np.linspace(-5,5,100)
ylist = func(xlist)

l.set_data(xlist,ylist)
plt.show()

metadata = dict(title='Movie', artist='codinglikemad')
writer = PillowWriter(fps=15, metadata = metadata)

xlist = []
ylist = []

with writer.saving(fig, "sinWave.gif", 100):
    for xval in np.linspace(-5,5,100):
        xlist.append(xval)
        ylist.append(func(xval))
        l.set_data(xlist,ylist)

        writer.grab_frame()

"""

#Lets now do the actual project
#Use a function from 3.1.3

#Function:

#Create a program which plots the tangent lines and estimations
#created by Newton's method on one plot and the secants and estimations
#by the secants methond on another plot for the same function

def f(x):
    return x**3 - 2*x - 5

def deriv(x):
    return 3*(x**2) - 2

x0 = 2.473684210526316
y0 = f(x0)

def tangent(x, x1, y1):
    return deriv(x1)*(x-x1) + y1

bounds = [0,3]

#First lets plot the original function and make it have two of them
#Side by side

X1 = np.arange(-1,4, .05)
Y1 = X1**3 - 2*X1 - 5

figure, axis = plt.subplots(2)

figure.suptitle("f(x) = x^3-2x-5, [a,b] = [0,3]")
axis[0].plot(X1,Y1)
axis[0].plot(X1, tangent(X1, x0, y0))
axis[0].set_title("Newton's Method: Tangent Lines and estimations")
axis[0].axhline(y=0, color='black')


axis[1].plot(X1,Y1)
axis[1].set_title("Secant Method: Tangent Lines and estimations")
axis[1].axhline(y=0, color='black')
plt.subplots_adjust(hspace = .4)

plt.show()



