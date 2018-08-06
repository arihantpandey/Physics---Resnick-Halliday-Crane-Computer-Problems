import math
def v(t):
    return math.exp((-(t**2))/100) * (1 + 10*math.sin(math.pi * t))
t = 0
dt = 0.001
distance = 0
k = 0
while(True):
    next_val = v(t+dt)
    distance += dt*(k+ next_val)/2
    k = next_val
    if (k < 0.000000001):
        break
    t += dt
print("v(t) = 0 at t =", t)
print("Distance from origin at time", t, "is", distance)
#finding value at infinity
t=1
while not((v(t)<0.001) and (v(t)>-0.001)):
    t += 2
final_time = t
print(final_time)
t = 0
dt = 0.1
distance = 0
while(t <= final_time):
    next_val = v(t+dt)
    distance += dt*(v(t)+ next_val)/2
    t += dt
print("Position at t = infinity is", distance)





