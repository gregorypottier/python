# Strings - Designer Door Mat

n, m = map(int, input().split(" "))

pattern = ".|."
patternList = []
# create patterns
for i in range(1, n, 2):
    patternList.append(pattern * i)
    
#top
for i in range(n // 2):
    print(patternList[i].center(m, "-"))

#middle
print("WELCOME".center(m, "-"))

#bottom
for i in range(len(patternList) - 1, -1, -1):
    print(patternList[i].center(m, "-"))
