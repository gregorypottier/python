# Built In - ginortS
s = input()

lower = [char for char in s if char.islower()]
lower.sort()

upper = [char for char in s if char.isupper()]
upper.sort()

digit = [char for char in s if char.isdigit()]
digit = sorted(digit, key = lambda x: (int(x)%2*-1, x)) # sorted on odd or even and then value

print("".join(lower + upper + digit))
