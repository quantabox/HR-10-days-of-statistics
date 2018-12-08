#!/usr/bin/env python

'''
Given integers  and , find the smallest integer , such that there exists a triangle of height , base , having an area of at least .

Input Format

In the first and only line, there are two space-separated integers  and , denoting respectively the base of a triangle and the desired minimum area.
'''

#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    return(math.ceil((2 * area) / base))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
