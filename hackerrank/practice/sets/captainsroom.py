# Sets - captains room
k, roomList = int(input()), list(map(int, input().split(" ")))
roomCount = {}
for roomNum in roomList:
    if roomNum in roomCount:
        roomCount[roomNum] += 1
    else:
        roomCount[roomNum] = 1

for roomNum in roomCount:
    if roomCount[roomNum] == 1:
        print(roomNum)
        break
