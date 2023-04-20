# Itertools - Permutation
def permutations(string, length):
    if length == 0:
        return [""]
    permutations_list = []
    for i in range(len(string)):
        char = string[i]
        remaining_string = string[:i] + string[i+1:]
        sub_permutations = permutations(remaining_string, length-1)
        for permutation in sub_permutations:
            permutations_list.append(char + permutation)
    return permutations_list

string, k = input().split(" ")
permutationLength = int(k)

plist = permutations(string, permutationLength)
plist.sort()
for p in plist:
    print(p)
