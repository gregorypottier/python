# Itertools - iterators and iterables
from itertools import combinations

length = int(input())
letters = input().split()
k = int(input())

allcombos = list(combinations(letters, k))
filteredCombos = list(filter(lambda combo: 'a' in combo, allcombos))
prob = round(len(filteredCombos)/len(allcombos), 3)
print(prob)
