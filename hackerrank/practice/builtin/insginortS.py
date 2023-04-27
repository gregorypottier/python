# builtin - InsginortS
s = input()

lower = [char for char in s if char.islower()]
lower.sort()

upper = [char for char in s if char.isupper()]
upper.sort()

digit = [char for char in s if char.isdigit()]
digit = sorted(digit, key = lambda x: int(x)%2*-1) # sort by either 0 or -1 depending on even or odd value

print("".join(lower + upper + digit))
