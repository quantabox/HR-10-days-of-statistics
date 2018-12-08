#!/usr/bin/env python

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day = 256-5*31-2*30
    isLeapYear = True if ((year <= 1917 and year % 4 == 0) or
                          (year > 1918 and
                           (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
                           )) else False
    day -= 15 if year == 1918 else 29 if isLeapYear else 28
    return "{0}.09.{1}".format(day, year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
