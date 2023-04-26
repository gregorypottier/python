# Errors and Exceptions - Exceptions
numTests = int(input())

for _ in range(numTests):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
