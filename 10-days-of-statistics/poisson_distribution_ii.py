#!/usr/bin/env python
# Approach I
def fact(y):
    if y <= 1:
        return 1
    return y*(fact(y-1))

poisson_random_variables = [float(x) for x in input().split()]

e = 2.71828
l_A = poisson_random_variables[0] # Machine A repair poisson random variable mean variance
l_B = poisson_random_variables[1] # Machine B repair poisson random variable mean variance

cost_A = 160 + 40 * (l_A + l_A**2)
cost_B = 128 + 40 * (l_B + l_B**2)

print("%.3f" % cost_A)
print("%.3f" % cost_B)

## Approach II
# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def poisson(?, k):
    return ? ** k * math.e ** (-?) / math.factorial(k)

def E(?):
    return ? + ? ** 2

?1, ?2 = map(float, input().split())

print("{:.3f}".format(160 + 40 * E(?1)))
print("{:.3f}".format(128 + 40 * E(?2)))
