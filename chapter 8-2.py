import math

v0 = 0
v = 0.00000000000000000001
m = 1
g = 9.8
dt = 0.001
t = 0
A = 2.4
B = 5.12
C  = -0.124
beta = 0.100
sum= 0

def phi(t):
    return (A + B*t+ C*t**3)*math.e**(-beta*t)

def angvel(t):
    return (phi(t+dt) - phi(t))/dt

while(angvel(t) > 0):
    t += dt
    sum += 0.5*(angvel(t)+angvel(t+dt))*dt

print("angvel is 0 at",t)
print(sum)
