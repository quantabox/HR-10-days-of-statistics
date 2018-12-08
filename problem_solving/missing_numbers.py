#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    while(arr):
        if(arr[0] in brr):
            brr_pop_index = brr.index(arr[0])
            arr.pop(0)
            brr.pop(brr_pop_index)
    brr.sort()
    return(sorted(set(brr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
