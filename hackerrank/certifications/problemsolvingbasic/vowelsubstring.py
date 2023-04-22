#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    l = len(s)
    k = int(k)
    ssIndex = -1
    maxVowelCount = 0
    vowelCount = 0
    for i in range(l):
        if i >= k and s[i-k] in "aeiou":
            vowelCount -= 1
        if s[i] in "aeiou":
            vowelCount += 1
        if i >= k-1 and vowelCount > maxVowelCount:
            maxVowelCount = vowelCount
            ssIndex = i - k + 1
    return s[ssIndex:ssIndex + k] if ssIndex != -1 else "Not found!"
        
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)
    if result == None:
        result = "greg"
    fptr.write(result + '\n')

    fptr.close()
