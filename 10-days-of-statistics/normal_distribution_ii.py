#!/usr/bin/env python

# Tutorials > 10 Days of Statistics > Day 5: Normal Distribution II
# Problems based on basic statistical distributions.
#
# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
# challenge id: 21230
#

import math


def N(x,  , s):
    """ Normal Distribution """
    p = math.pi
    return math.exp(- (x -  ) ** 2 / (2 * s * s)) / (s * math.sqrt(2 * p))


def F(x,  , s):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x -  ) / s / math.sqrt(2)))


 , s = map(float, input().split())
q1 = float(input())
q2 = float(input())

# percentage of students having grade > q1
print("{:.2f}".format(100 - F(q1,  , s) * 100))

# percentage of students having grade = q2
print("{:.2f}".format(100 - F(q2,  , s) * 100))

# percentage of students having grade < q2
print("{:.2f}".format(F(q2,  , s) * 100))
