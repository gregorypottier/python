import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    
    letters = [] # letters contains middle portion of each row
    for i in range(size):
        sub_alphabet = alphabet[i:size] # subset alphabet to appropriate characters
        letters.append("-".join(sub_alphabet[::-1] + sub_alphabet[1:]))
    # top 
    for i in range(size - 1, 0, -1): # start at size, go down 1, stop at 0
        print(letters[i].center(4 * size - 3, "-"))
    # center 
    print(letters[0].center(4 * size - 3, "-"))
    # bottom 
    for i in range(1, size):
        print(letters[i].center(4 * size - 3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
