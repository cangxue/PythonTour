
#数学库math
from math import *
from random import *
from time import clock

print(pi)
f = pi
c1 = ceil(f)
c2 = floor(f)
c3 = pow(2,3)
c4 = log(4)
c5 = log2(4)
c6 = sqrt(16)
print(c1,c2,c3,c4,c5,c6)
#4 3 8.0 1.3862943611198906 2.0 4.0

x = 4
y = 60
d1 = exp(x)
d2 = degrees(x)
d3 = radians(x)
d4 = sin(y)
d5 = cos(y)
d6 = tan(y)
d7 = asin(1)
d8 = acos(1)
d9 = atan(1)
print(d1, d2, d3, d4, d5, d6, d7, d8, d9)
#54.598150033144236 229.1831180523293 0.06981317007977318 -0.3048106211022167
#-0.9524129804151563 0.3200403893795629 1.5707963267948966 0.0 0.7853981633974483

#随机数库random
seed(10)
r1 = random()
r2 = uniform(0, 100)
r3 = randint(0, 100)
r4 = randrange(0, 100, 5)
ra = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r5 = choice(ra)
print(r1, r2, r3, r4, r5)
#0.5714025946899135 42.888905467511464 73 0 3

r6 = shuffle(ra)
print(ra)
#[2, 8, 6, 3, 0, 1, 5, 4, 9, 7]

r7 = sample(ra, 5)
print(r7)
#[3, 1, 2, 7, 8]

DARTS = 1200
hits = 0
clock()
for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi = %s" % pi)
print("time = %-5.ess" % clock())