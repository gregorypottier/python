# Functionals - map and lambda
cube = lambda x: x**3

def fibonacci(n):
    num1 = 0
    num2 = 1
    fibs = []
    for i in range(n):
        fibs.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return fibs

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
