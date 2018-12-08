#!/usr/bin/env python

#!/bin/python3
from __future__ import print_function
import os
import sys
from functools import reduce
#
# Complete the connectingTowns function below.

# Approach I
def connectingTowns(n, routes):
    return reduce(lambda x, y: x * y, routes, 1) % 1234567

# Approach II
def connectingTowns(n, routes):
    temp=1
    i=0
    while (i<n-1):
        temp=temp*routes[i]
        i+=1
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
