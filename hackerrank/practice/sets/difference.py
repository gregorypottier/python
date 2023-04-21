# Sets - difference
input()
roll1 = list(map(int, input().split(" ")))
input()
roll2 = list(map(int, input().split(" ")))

print(len(set([element for element in roll1 if element not in roll2])))
