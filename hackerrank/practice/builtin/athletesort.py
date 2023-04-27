# Built in - athlete sort
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())) + [i])
        
    k = int(input())

    sorter = lambda x : (x[k], x[-1])
    
    arr = sorted(arr, key = sorter)
    for element in arr:
        print(" ".join(map(str, element[:-1])))
    
