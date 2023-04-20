import numpy as np

n, m, p = map(int, input().split(" "))
rows = n + m
cols = p

arr = np.array([], dtype=int)

for i in range(rows):
    tempArr = np.array(list(map(int, input().split(" "))))
    arr = np.concatenate((arr, tempArr), axis=0)
    
arr = arr.reshape((rows, cols))
print(arr)
