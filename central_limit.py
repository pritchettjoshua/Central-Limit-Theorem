__author__ = 'Joshua Pritchett'
import random
import math
heads = 0
tails = 0
n = 4
t = 2
while t <= 24:
    for i in range(0, n):
        if random.random() >= 0.5:
            heads += 1
        else:
            tails += 1
    print('{0:10d} {1:10d} {2:10f} {3:10f}'.format(n, abs(heads-tails), (abs(heads-tails))/math.sqrt(n), (abs(heads-tails))/n))
    heads = 0
    tails = 0
    t += 1
    n = pow(2,t)













