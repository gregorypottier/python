# Collections - Word Order
from collections import OrderedDict

numWords = int(input())
wordCounts = OrderedDict()  
for i in range(numWords):
    string = input()
    if string in wordCounts.keys():
        wordCounts[string] += 1
    else:
        wordCounts[string] = 1

uniqueKeys = len(set([key for key in wordCounts.keys()]))
print(uniqueKeys)
print(*wordCounts.values()) # unpack values
    
