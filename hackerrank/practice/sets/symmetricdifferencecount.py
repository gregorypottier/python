# Sets - Symetric Difference Operation
input()
roll1 = set(map(int, input().split(" ")))
input()
roll2 = set(map(int, input().split(" ")))
print(len(set([entry for entry in roll1 if entry not in roll2] + [entry for entry in roll2 if entry not in roll1])))
