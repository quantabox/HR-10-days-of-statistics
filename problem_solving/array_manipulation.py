#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for (p, q, sum) in queries:
        arr[p]+=sum
        if (q+1<=n): 
            arr[q+1]-=sum
    max_value = 0
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i]
        max_value = max(max_value, sum)
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
