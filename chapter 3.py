import math
import matplotlib.pyplot as plt

v0 = 50
v1 = v0
m = 10
g = 9.8
t = 0
dt = 0.01
b = 10
s = 0
time = []
position = []

while(s>=0):
    t += dt
    time.append(t)
    k = v1
    v1 = v1 + (-b*v1/m - g)*dt

    s += dt*(k + v1)/2
    position.append(s)
    print("at time", t, "the position is", s)

plt.plot(time, position)
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.title("b="+ str(b))
plt.show()
