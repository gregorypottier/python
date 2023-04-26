# Date and Time - timedelta
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    a=datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    b=datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    secondsApart = int(abs(a -b).total_seconds())
    return secondsApart

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')

    fptr.close()
