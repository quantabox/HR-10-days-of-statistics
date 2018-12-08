#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys
import copy

min_cost = sys.maxsize

def checkCost(rotated_arr, test_case):
    global min_cost
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(int(test_case[i][j]) - int(rotated_arr[i][j]))
    if cost < min_cost:
        min_cost = cost


def rotate_90_arr(arr, test_case):
    rotated_arr = copy.deepcopy(arr)
    for i in range(4):
        # slice multi-dimensional array vertically
        list_of_tuples = zip(*rotated_arr[::-1]) 
        rotated_arr = [list(elem) for elem in list_of_tuples]
        checkCost(rotated_arr, test_case)


# Complete the formingMagicSquare function below.
def formingMagicSquare(test_case):
    """
    magic_square : 3 x 3 magic_square matrix
    symmetry_arr : top and Bottom Symmetrical matrix
    * a[::-1]  : a = [1,2,3] => [3,2,1]
    """
    magic_square = [[8,3,4],[1,5,9],[6,7,2]]
    symmetry_arr = magic_square[::-1]
    rotate_90_arr(magic_square, test_case)
    rotate_90_arr(symmetry_arr, test_case)
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
