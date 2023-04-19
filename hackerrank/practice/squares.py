if __name__ == '__main__':
    n = int(input())
    square_generator = (num**2 for num in range(n))
    for num in square_generator:
        print(num)
