import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig, (ax1, ax2) = plt.subplots(2)
tLine, = ax1.plot([], [])
sLine, = ax2.plot([], [])

line = [tLine, sLine]

for ax in [ax1, ax2]:
    ax.set_ylim(-10,30)
    ax.set_xlim(0,3)

def func(x):
    return (x**3)-(2*x)-5

xlist = np.linspace(0,3,100)
ylist = func(xlist)

ax1.set_title("Newton's Method: Tangent Lines and estimations")
ax1.axhline(y=0, color='black')
ax1.plot(xlist, ylist)

ax2.set_title("Secant: Lines and estimations")
ax2.axhline(y=0, color='black')
ax2.plot(xlist, ylist)

plt.subplots_adjust(hspace = .4)

def newtons(x0, err):
    xList = [x0]
    newtonErr = xList[0]

    i = 0
    while(newtonErr > err):
        xList.append(xList[i] - (func(xList[i])/deriv(xList[i])))
        i = i + 1
        newtonErr = abs(xList[i] - xList[i-1])
    return xList

def deriv(x):
    return 3*(x**2) - 2

def tangent(x, x1, y1):
    return deriv(x1)*(x-x1) + y1

def secant(x0, x1, err):
    xList = [x0, x1, x0 - (x1-x0)*func(x0)/( func(x1) - func(x0))]
    secantErr = abs(func(xList[2]))

    i = 2
    while(secantErr > err):
        xList.append(xList[i-1] - (xList[i]-xList[i-1])*func(xList[i-1])/( func(xList[i]) - func(xList[i-1])))
        i = i + 1
        secantErr = abs((xList[i]) - (xList[i-1]))
    print(xList)
    return xList

def secantLine(x, x1, x2):
    return (((func(x2)-func(x1))/(x2-x1))*x) - ((((func(x2)-func(x1))/(x2-x1))*x2)-func(x2))

x0 = 1.5
y0 = func(x0)
err = 10**-5

secx1 = 1.5
secx2 = 1.75

newtonList = newtons(x0, err)

secantList = secant(secx1, secx2, err)

writer = PillowWriter(fps=10)

with writer.saving(fig, "testerFN.gif", 100):
    
    for i in newtonList:
        xlist = []
        ylist = []
        y0 = func(i)
        for xval in np.linspace(0,3,100):
            xlist.append(xval)
            ylist.append(tangent(xval, i, y0))
            line[0].set_data(xlist,ylist)
            writer.grab_frame()

    for i in secantList:
        x2list = []
        y2list = []
        for xval in np.linspace(0, 3, 100):
            x2list.append(xval)
            y2list.append(secantLine(xval, i, i+1))
            line[1].set_data(x2list,y2list)
            writer.grab_frame()

print('Finish')
