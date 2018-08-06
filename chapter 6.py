import math

vratio = 1
m4 = 10
m1 = 640
m3 = 1
m2 = 1
g = 9.8
dm = 0.01
vf1 = 0
vf2 = 0.00000000000000000001
v0 = -1

# m1 = 1
# m2 = 288
# m3 =  102
# m4 = 37
# v1f = -v0
# v2f = 2 * m1 * v1f / (m1 + m2) + (m2 - m1) * v0 / (m2 + m1)
# v3f = 2 * m2 * v2f / (m2 + m3) + (m3 - m2) * v0 / (m2 + m3)
# v4f = 2 * m3 * v3f / (m4 + m3) + (m4 - m3) * v0 / (m4 + m3)
# print(v4f)


MAX = 0
for i in range(1,640,1):
    for j in range(1,i,1):
        m2 = i
        m3 = j
        v1f = -v0
        v2f = 2 * m1 * v1f / (m1 + m2) + (m2 - m1) * v0 / (m2 + m1)
        v3f = 2 * m2 * v2f / (m2 + m3) + (m3 - m2) * v0 / (m2 + m3)
        v4f = 2 * m3 * v3f / (m4 + m3) + (m4 - m3) * v0 / (m4 + m3)

        if (v4f > MAX):
            MAX = v4f
            maxm2 = m2
            maxm3 = m3
        print(v2f, v3f, v4f)

print(maxm2, maxm3)


