#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lows = 0
    highs = 0
    for i in range(1, len(scores)):
        if scores[i] < min(scores[:i]): #min
            lows += 1
        elif scores[i] > max(scores[:i]): #max
            highs += 1
    return highs, lows 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
