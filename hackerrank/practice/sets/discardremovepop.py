# Sets - discard, remove, pop

input()
originalSet = set(list(map(int, input().split(" "))))
numOperations = int(input())
for i in range(numOperations):
    command = list(input().split(" "))
    try:
        if len(command) == 2:
            num = int(command[1])
            eval(f"originalSet.{command[0]}({num})")
        else:
            eval(f"originalSet.{command[0]}()")
    except:
        continue
            
print(sum(originalSet))
