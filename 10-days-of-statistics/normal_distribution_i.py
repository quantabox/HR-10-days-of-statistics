#!/usr/bin/env python

import math

p = math.pi


def N(x, µ, s):
    """ Normal Distribution """
    return math.exp(- (x - µ) ** 2 / (2 * s * s)) / (s * math.sqrt(2 * p))


def F(x, µ, s):
    """ Cumulative Probability """
    return 1 / 2 * (1 + math.erf((x - µ) / s / math.sqrt(2)))


µ = 20
s = 2

print("{:.3f}".format(F(19.5, µ, s)))

print("{:.3f}".format(F(22, µ, s) - F(20, µ, s)))

