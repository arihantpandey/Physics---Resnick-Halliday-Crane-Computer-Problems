import math
import matplotlib.pyplot as plt

mi = 4000
mf = 27000
fr = 230
sg = 2500
g = 9.8
re = 6371000
y = 0.00001
distance = []
times = []
t = 0
dt = 0.01
v0 = 0
vf = 0
burnouttime = 0

def g(y):
    return 9.8*(re/(re+y))**2

def m(t):
    m = mi + mf - fr*t
    if m >= mi:
        return m
    else:
        return mi

def findburnouttime():
    t = 0
    m = mi + mf
    while m >= mi:
        m -= fr * dt
        t+=dt
    print("burnouttime: ", t)
def anet(t, m, g):
    if m == mi:
        return -g
    else:
        return (sg*fr - m*g)/m

def vertdist(t, v0, vf):
    return dt*(v0 + vf)/2

while t <= mf/fr:
    vf = v0 + anet(t, m(t), g(y))*dt
    y += vertdist(t, v0, vf)
    distance.append(y)
    times.append(t)
    # print(y, t)
    t+=dt
    v0 = vf

print(mf/fr)
print(vf)
print(y)




v0 = 0
vf = 0
y = 0
t = 0
while vf >=0:
    vf = v0 + anet(t, m(t), g(y))*dt
    y += vertdist(t, v0, vf)
    distance.append(y)
    times.append(t)
    # print(y, t)
    t+=dt
    v0 = vf

print(y)

#
# plt.plot(times, distance)
# plt.ylabel('position (m)')
# plt.xlabel('t(s)')
# plt.title("graph")
# plt.show()