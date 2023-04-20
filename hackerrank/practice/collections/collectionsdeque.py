# Collections - Collections.deque
from collections import deque

numOperations = int(input())
d = deque()
for i in range(numOperations):
    command = input().split(" ")
    if len(command) == 2:
        eval(f"d.{command[0]}({command[1]})")
    else:
        eval(f"d.{command[0]}()")
print(*d) # unpack deque and print
