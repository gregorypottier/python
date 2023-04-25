# Collections - defaultdict
sizeN, sizeM = map(int, input().split())

dictionary = {}
for i in range(1, sizeN+1):
    word = input()
    if word in dictionary:
        dictionary[word].append(str(i))
    else:
        dictionary[word] = [str(i)]

for i in range(sizeM):
    word = input()
    if word in dictionary:
        print(" ".join(dictionary[word]))
    else:
        print(-1)
