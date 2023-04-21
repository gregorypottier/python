# Sets - no idea
input()
originalList = list(map(int, input().split(" ")))
like = set(map(int, input().split(" ")))
dislike = set(map(int, input().split(" ")))
happiness = 0
print(sum([1 if item in like else 0 for item in originalList] + 
[-1 if item in dislike else 0 for item in originalList]))
