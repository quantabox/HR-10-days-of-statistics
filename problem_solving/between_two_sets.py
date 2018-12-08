#!/usr/bin/env python

#!/bin/python3

import os
import sys
from functools import reduce
#
# Complete the getTotalX function below.
#
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)    

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm,min_gcd+1,max_lcm) if min_gcd % x == 0])
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
