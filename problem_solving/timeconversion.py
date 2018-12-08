#!/usr/bin/env python

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hours, minutes, rest = s.split(':')
    hours = int(hours)
    seconds = rest[:2]
    ampm = rest[2:]
    if hours == 12:
        if ampm == 'AM':
            hours = 0
    else:
        if ampm == 'PM':
            hours = (hours + 12)

    return "%02d:%s:%s" %(hours, minutes, seconds)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
