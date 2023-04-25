# Collections - company logo

import math
import os
import random
import re
import sys
    
if __name__ == '__main__':
    name = input()

    dictionary = {}
    for char in name:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
            
    sorter = lambda x: (x[1] * -1, x[0]) # -1 is used to make sorting order of count descending
    top3 = sorted(dictionary.items(), key=sorter)[:3] 

    for char, count in top3:
        print(char, count)

