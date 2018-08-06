import math
import matplotlib.pyplot as plt

m = 2.5
v0 = 150
v = v0
theta = 40*math.pi/180
v0x = v0*math.cos(theta)
v0y = v0*math.sin(theta)
vx= v0x
vy = v0y
b = 0.50
dt = 0.5
g = 9.8
t = 0

vxvalues = []
vyvalues = []
times = []

def a(v):
    return (m*(-g)-b*v)/m

print(m*g/b)
print(v*math.cos(theta))

while(vy > 0.9*(-m*g/b)):
    vx += -b*(v0x)*dt/m
    vy += a(v0y)*dt
    print(vx, vy)
    vxvalues.append(vx)
    vyvalues.append(vy)
    v0x = vx
    v0y = vy
    times.append(t)
    t+=dt



plt.plot(times, vxvalues)
plt.plot(times, vyvalues)
plt.ylabel('v')
plt.xlabel('t(s)')
plt.title("graph")
plt.show()
