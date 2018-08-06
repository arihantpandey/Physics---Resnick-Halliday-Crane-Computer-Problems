m = 0.15
v0 = 25
v = v0
h = 300
b = 0.015
g = 9.8
dt = 0.001
pos = h
t = 0

def D(v):
    return b*v/m

while(pos > 0):
    a = -g - D(v)
    v = v0 + a*dt
    pos += 0.5*dt*(v0 + v)
    v0 = v
    t+=dt

print("time taken:", t)
print("final velocity:", v)

m = 0.15
v0 = 25
v = v0
h = 300
b = 0.015
g = 9.8
dt = 0.001
pos = h
t = 0
a = -10

while(a<-0.001):
    a = -g - D(v)
    print(a)
    v = v0 + a*dt
    #pos += 0.5*dt*(v0 + v)
    v0 = v


print("terminal velocity:", v)