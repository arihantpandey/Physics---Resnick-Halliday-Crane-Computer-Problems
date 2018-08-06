import math

v0 = 0
v = 0.00000000000000000001
m = 95
g = 9.8
Ffr = 80
dt = 0.01
t = 0
s = 0

def F(t):
    return 200*math.e**(-0.15*t)

while(v>0):
    v = v0 + dt*(F(t)-80)/95
    s += 0.5*(v + v0)*dt
    v0 = v
    t += dt

print("total time:", t)
print("total distance:", s)
