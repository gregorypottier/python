if __name__ == '__main__':
    pairs = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        pairs.append([name, score])
        
    nextLowest = sorted(set([score for name, score in pairs]))[1] # list to set for unique values only, sort ascending, retrieve second value
    pairs.sort() # in place sort
    for name, score in pairs:
        if score == nextLowest:
            print(name)

