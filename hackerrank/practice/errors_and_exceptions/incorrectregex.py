# Erros and Exceptions - incorrect regex
import re
numTests = int(input())

for _ in range(numTests):
    regex = input()
    try:
        re.compile(regex)
        print("True")
    except re.error:
        print("False")
