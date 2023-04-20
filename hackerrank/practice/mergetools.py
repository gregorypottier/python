def removeduplicate(string):
    result = ""
    seen = set()
    for char in string:
        if char not in seen:
            result += char
            seen.add(char)
    return result

def merge_the_tools(string, k):
    substrings = []
    i = 0
    j = k
    for _ in range(0, int(len(string)/k)):
        ss = string[i:j]
        substrings.append(ss)
        i+= k
        j += k
        
    resultList = [removeduplicate(ss) for ss in substrings]
    for string in resultList:
        print(string)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
