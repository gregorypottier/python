# String - Minion Game

def minion_game(string):
    length = len(string)
    vcount = 0
    ccount = 0
     
    for i in range(length):
        if string[i].upper() in "AEIOU":
            vcount = vcount + (length - i) # number of substrings that can be formed with the remaining characters after the current character
        else:
            ccount = ccount + (length - i) 
                
    if vcount < ccount:
        print("Stuart", str(ccount))
    elif vcount > ccount:
        print("Kevin", str(vcount))
    else:
        print("Draw")
        
            
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
