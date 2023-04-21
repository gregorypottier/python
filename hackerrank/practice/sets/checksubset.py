# Sets - Check Subset
numComparisons = int(input())

for i in range(numComparisons):
    dummy, set1 = input(), set(map(int, input().split(" ")))
    dummy, set2 = input(), set(map(int, input().split(" ")))
    print(all([entry in set2 for entry in set1]))
