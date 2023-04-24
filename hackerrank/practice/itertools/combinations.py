# Itertools - combinations
def combination(charList, k):
    if k == 0:
        return [[]]
    combos =[]
    for index, first_char in enumerate(charList):
        selected_char = first_char
        # Generate all possible combinations of length k-1 from the remaining characters.
        remaining_chars = charList[index + 1:]
        remaining_combos = combination(remaining_chars, k-1)
        # Add the selected character to each of the k-1 length combinations generated above.
        for remaining_combo in remaining_combos:
            new_combo = [selected_char, *remaining_combo]
            new_combo.sort()
            combos.append(new_combo)
    combos.sort()
    return combos
 
string, k = input().split()
k = int(k)
for i in range(1, k + 1):
    result = combination([x for x in string], i)
    for combo in result:
        print("".join(combo))
