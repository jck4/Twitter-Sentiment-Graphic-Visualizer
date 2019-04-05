import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from decimal import *

style.use("ggplot")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-Sentiment.txt","r").read()
    lines = pullData.split("\n")
    lines.remove('')

    xar = []
    yar = []

    x = 0
    y = 0


    for line in lines[-50:]:
        x += 1
        y += float(line)

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
