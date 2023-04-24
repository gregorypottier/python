# Itertools - maximize it
from itertools import product

k, mod = map(int, input().split(" "))

ll = []

for i in range(k):
    sl = list(map(lambda x: int(x)**2, input().split(" ")[1:])) # first number indicates size
    ll.append(sl) # append squared values to ll
# cartesian product of all the sublists and computing the remainder of their sum when divided by m
allProducts = list(product(*ll))
results = list(sum(x) % mod for x in allProducts)
print(max(results))
