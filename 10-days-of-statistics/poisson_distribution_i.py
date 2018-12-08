#!/usr/bin/env python

# Question: A random variable, X, follows Poisson distribution with mean of 2.5
# Find the probability with which the random variable X is equal to 5.

# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

# Set data
mean = float(input())
k = float(input())
e = 2.71828

# Gets the result and show on the screen
result = ((mean ** k) * (e ** -mean)) /  factorial(k)
print(round(result, 3))

### Approach II
import math


def poisson(k, lam):
    return round(
        (math.pow(lam, k) * math.pow(math.e, -lam)) / math.factorial(k), 3)


def poisson_bootstrap(k, lam, experiments=100000):
    """Unsure how to do this w/o numpy"""
    pass


def test_poisson():
    lam = 2.5
    k = 5

    assert poisson(lam=lam, k=k) == 0.067
    # assert round(poisson_bootstrap(lam=lam, k=k), 2) == 0.07


if __name__ == '__main__':
    lam = float(input())
    k = int(input())

    print(round(poisson(k=k, lam=lam), 3))
