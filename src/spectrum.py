import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frame):
    plt.clf()
    plt.axis("off")  # delete axis
    plt.ylim(-2,2)   # define Y-axis limit
    x = np.linspace(0, 20*np.pi, 2000) # define X-array
    y1 = np.sin(x + float(frame)/100.0) # caluclate Y value for each X value
    plt.plot(x,y1,'gray')
    y2 = 0.5*np.sin(x + float(frame)/50.0)
    plt.plot(x,y2,'silver')
    #plt.plot(x,y1+y2,'snow')

#plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.axis("off")
plt.tight_layout()
plt.ylim(-2,2)
fig = plt.figure(figsize=(20,2),facecolor="black") # define image size (20*100 px, 2*100 px) & set background-color

ani = animation.FuncAnimation(fig, update, frames=range(0,2*314,10), interval=50)

#plt.show() # display gif on another window

w = animation.PillowWriter(fps=60)
ani.save('./animation.gif', writer=w)
