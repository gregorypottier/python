# numpy - zeros and ones
import numpy as np
shape = list(map(int, input().split(" ")))

arr0 = np.zeros(shape , dtype=int)
print(arr0)
arr1 = np.ones(shape , dtype=int)
print(arr1)
