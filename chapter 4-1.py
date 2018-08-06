import math
import matplotlib.pyplot as plt

def Fx(x):
    return -20*x
def Fy(y):
    return -20*y

m = 5
x = 2
y = 0
v0x = 0
vx = v0x
v0y = 20
vy = v0y
dt = 0.001
t = 0

xvalues = []
yvalues = []

while(t<4):
    ax = Fx(x)/m
    ay = Fy(y)/m
    vx = v0x + ax*dt
    vy = v0y + ay*dt
    x += 0.5*dt*(v0x+vx)
    y += 0.5*dt*(v0y+vy)
    xvalues.append(x)
    yvalues.append(y)
    t += dt
    v0y = vy
    v0x = vx

plt.plot(xvalues, yvalues)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title("graph")
plt.show()
