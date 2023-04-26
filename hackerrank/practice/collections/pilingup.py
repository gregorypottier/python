# Collections - Piling up
def isvalidstack(stack):
    i = 0
    for j in range(1, len(stack)):
        if stack[i] < stack[j]:
            return "No"
        i += 1
    return "Yes"
            
def stack(l):
    length = len(l)
    tempStack = []
    for i in range(length):
        leftmost = l[0]
        rightmost = l[-1]
        if leftmost >= rightmost:
            tempStack.append(l.pop(0))
        else:
            tempStack.append(l.pop(-1))
    return isvalidstack(tempStack)
 
numCubes = int(input())

truthList = []
for i in range(numCubes):
    l = int(input())
    cubes = list(map(int, input().split()))
    truthList.append(stack(cubes))
for ans in truthList:
    print(ans)
