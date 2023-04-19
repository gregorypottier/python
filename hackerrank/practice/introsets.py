# Sets - Intro to sets
def average(array):
    numList = list(set(array))
    return sum(numList) / len(numList)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
