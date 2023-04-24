# Itertools - combinations with replacement
from itertools import combinations_with_replacement

string, k = input().split()
k = int(k)
result = combinations_with_replacement(string, k)
result = sorted(["".join(sorted(element)) for element in result])
print("\n".join(result))
