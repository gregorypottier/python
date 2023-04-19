if __name__ == '__main__':
    N = int(input())
    numberList = []
    for _ in range(N):
        s = input().strip().split(" ")
        command = s[0]
        args = s[1:]
        if command != "print":
            joinedArgs = ", ".join(args)
            totalCommand = f"numberList.{command}({joinedArgs})"
            eval(totalCommand) # evaluates string as executionable code
        else:
            print(numberList)
