# Built in - any or all
numbers, numList= int(input()), list(map(int, input().split()))
condition1 = all(x > 0 for x in numList) # all must be positive
condition2 = any(str(x) == str(x)[::-1] for x in numList) # any could be palindromic
print(condition1 and condition2)
