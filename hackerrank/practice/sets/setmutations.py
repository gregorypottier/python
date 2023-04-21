# Sets - set mutations
input()
originalSet = set(map(int, input().split(" ")))
numOperations = int(input())
for i in range(numOperations):
    command = input().split(" ")
    tempSet = set(map(int, input().split(" ")))
    eval(f"originalSet.{command[0]}({tempSet})")
print(sum(originalSet))
