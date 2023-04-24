# Collections - counter

numShoes, sizes, numCustomers = int(input()), map(int, input().split()), int(input())

inventoryDict = {}
for size in sizes:
    if size in inventoryDict:
        inventoryDict[size] += 1
    else:
        inventoryDict[size] = 1

totalSales = []
for _ in range(numCustomers):
    size, price = map(int, input().split())
    if size in inventoryDict and inventoryDict[size] > 0:
        totalSales.append(price)
        inventoryDict[size] -= 1
        
print(sum(totalSales))
    

