#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    a_count = 0
    b_count = 0
    zipped_score = zip(a, b)
    for pair in zipped_score:
        if pair[0] > pair[1]:
            a_count += 1
        elif pair[0] < pair[1]:
            b_count += 1
    return a_count, b_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
