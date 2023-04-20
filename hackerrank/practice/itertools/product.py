# Itertools - product

A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
for element in [(x,y) for x in A for y in B]:
    print(element, end = " ")
