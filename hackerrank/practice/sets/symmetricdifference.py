# Sets - Symmetric Difference
input() # clear stdin
m = set(map(int, input().split(" ")))
input()
n = set(map(int, input().split(" ")))
exclusiveM = [entry for entry in m if entry not in n]
exclusiveN = [entry for entry in n if entry not in m]
result = exclusiveN + exclusiveM
result.sort()
for entry in result:
    print(entry)
