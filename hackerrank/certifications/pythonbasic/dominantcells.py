#!/bin/python3

import math
import os
import random
import re
import sys

def dominant(grid, i, j):
    value = grid[i][j]
    for row in range(max(0, i-1), min(i+2, len(grid))):
        for col in range(max(0, j-1), min(j+2, len(grid[0]))):
            if (row != i or col != j) and grid[row][col] >= value:
                return False
    return True

def numCells(grid):
    result = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dominant(grid, i, j):
                result.append((i, j))
    return len(result)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
