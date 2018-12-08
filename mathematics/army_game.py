#!/usr/bin/env python

'''
Luke is daydreaming in Math class. He has a sheet of graph paper with n rows and m  columns, and he imagines that there is an army base in each cell for a total of
n.m bases. He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. 
If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:


Given n and m , what's the minimum number of packages that Luke must drop to supply all of his bases?

Input Format

Two space-separated integers describing the respective values of n and m .
'''

#!/bin/python3

import os
import sys
import math 
#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):
    return (math.ceil(n/2)*math.ceil(m/2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
