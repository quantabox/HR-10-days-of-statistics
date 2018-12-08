#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

def leftRotation(a, d):
    # Complete this function
    for i in range(0, d):
        popped = a.pop(0)
        a.append(popped)
    return a

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
