from collections import OrderedDict

numItems = int(input())
ordered_dictionary = OrderedDict()

for i in range(numItems):
    data = input().split(" ")
    price = int(data[-1])
    name = " ".join(data[:-1])
    if name in ordered_dictionary.keys():
        ordered_dictionary[name] = ordered_dictionary[name] + price
    else:
        ordered_dictionary[name] = price
        
for key, value in ordered_dictionary.items():
    print(key, value)
