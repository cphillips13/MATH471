from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation

figure, axis = plt.subplots()

x, y = [],[]

line, = axis.plot(0,0)

def func(x):
    return (x**3)-(2*x)-5

def animate(frame):
    x.append(frame)
    y.append(frame)
    line.set_xdata(x)
    line.set_ydata(func(x))
    return line,

anim = animation.FuncAnimation(figure, animate, frames = 100, interval=1 , blit = True)

writervideo = animation.FFMpegWriter(fps = 60)
anim.save('testingtangent.mp4',writer = writervideo)
plt.close()