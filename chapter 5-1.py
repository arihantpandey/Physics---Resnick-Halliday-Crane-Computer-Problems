


m = 200
g = 9.8
us = 0.60
uk = 0.50
l = 10
vcar = 5
vbox = 0
boxdist = 0
dt = 0.1
t = 0
k = 0

times = []
distance = []


def a(l):
    if l > 10:
        return 400*(l-10)/m
    else:
        return 0

def anet(l):
    return 400*(l-10)/m - g*uk

def staticfric(l,t):
    while(a(l) < g*us):
        l += vcar*dt
        t+=dt
        times.append(t)
        distance.append(0)

while(t < 10):
    oldk = k
    t+=dt
    l+= vcar*dt
    if vbox > 0:
        k = anet(l)
    else:
        k = a(l)
    vbox += 0.5*(k+oldk)
    if vbox < 0:
        vbox = 0
    l-= (vbox)*dt
    boxdist += vbox*dt
    distance.append(boxdist)
    times.append(t)
    print(boxdist, vbox, l)

plt.plot(times, distance)
plt.ylabel('position (m)')
plt.xlabel('t(s)')
plt.title("graph")
plt.show()