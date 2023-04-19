# Strings - swapcase
def swap_case(s):
    string = [char.upper() if char.islower() else char.lower() for char in s]
    return "".join(string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
