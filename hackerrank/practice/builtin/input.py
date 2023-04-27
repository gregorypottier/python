# Built in - input
x, k = map(int, input().split())
polynomial = input()
polynomial = "".join(str(x) if char == "x" else char for char in polynomial)
print(eval(polynomial) == k)
