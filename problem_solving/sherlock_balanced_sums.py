#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
  left = 0
  right = sum(arr)
  
  for i in range(len(arr)):
    right -= arr[i]
    
    if left == right:
      return ("YES")
    
    left += arr[i]
    
  return ("NO")
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
