# Sets - check strict superset
set1 = set(map(int, input().split(" ")))
extraSets = int(input())
boolArr = []
for i in range(extraSets):
    tempSet = set(map(int, input().split(" ")))
    result = all([(element in set1) and (len(tempSet) < len(set1)) for element in tempSet])
    boolArr.append(result)
print(all(boolArr))
