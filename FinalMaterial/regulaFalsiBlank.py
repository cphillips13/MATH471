import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

figure, axis = plt.subplots(2)

l, = plt.plot([], [], 'k-')

plt.xlim(0,3)
plt.ylim(-10,30)

def func(x):
    return (x**3)-(2*x)-5

def deriv(x):
    return 3*(x**2) - 2

x0 = 1.5
y0 = func(x0)

def tangent(x, x1, y1):
    return deriv(x1)*(x-x1) + y1

xlist = np.linspace(0,3,100)
ylist = func(xlist)

axis[0].set_title("Newton's Method: Tangent Lines and estimations")
axis[0].axhline(y=0, color='black')
axis[0].plot(xlist, ylist)
l.set_data(xlist,ylist)

axis[1].set_title("Secant: Lines and estimations")
axis[1].axhline(y=0, color='black')
axis[1].plot(xlist, ylist)

plt.show()

metadata = dict(title='Movie', artist='codinglikemad')
writer = PillowWriter(fps=60, metadata = metadata)

xlist = np.linspace(0,3,100)
ylist = func(xlist)
l.set_data(xlist,ylist)

xlist = []
ylist = []

def newtons(x0, runTime):
    xList = [x0]
    for i in range(runTime):
        xList.append(xList[i] - (func(xList[i])/deriv(xList[i])))
    return xList

runtime = 5
newtonList = newtons(x0, runtime)

with writer.saving(figure, "testerFN.gif", 100):
    for i in range(runtime):
        xlist = []
        ylist = []
        x0 = newtonList[i]
        y0 = func(x0)
        for xval in np.linspace(0,3,100):
            xlist.append(xval)
            ylist.append(tangent(xval, x0, y0))
            l.set_data(xlist,ylist)
            writer.grab_frame()
        

