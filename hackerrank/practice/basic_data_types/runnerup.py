if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runnerUp = max([element for element in arr if element != max(arr)])
    print(runnerUp)
