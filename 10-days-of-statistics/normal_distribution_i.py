#!/usr/bin/env python

import math

p = math.pi


def N(x, �, s):
    """ Normal Distribution """
    return math.exp(- (x - �) ** 2 / (2 * s * s)) / (s * math.sqrt(2 * p))


def F(x, �, s):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - �) / s / math.sqrt(2)))


� = 20
s = 2

print("{:.3f}".format(F(19.5, �, s)))

print("{:.3f}".format(F(22, �, s) - F(20, �, s)))

