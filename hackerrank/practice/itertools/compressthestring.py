# Itertools - compress the string
string = input()

count = 1
result = []
for i in range(len(string) - 1):
    countChar = string[i]
    compareChar = string[i + 1]
    if countChar != compareChar:
        result.append((count, int(countChar)))
        count = 1
    elif countChar == compareChar:
        count += 1
result.append((count, int(string[-1]))) # last case is handled alone. no compareChar (index out of bounds error)
for element in result:
    print(element, end = " ")
