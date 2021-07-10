boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
ans = 0
for i in range(len(boxTypes)):
    if truckSize >= boxTypes[i][0]:
        truckSize -= boxTypes[i][0]
        ans += (boxTypes[i][0]*boxTypes[i][1])
    elif truckSize == 0:
        break
    else:
        ans += (boxTypes[i][1]*truckSize)
        truckSize = 0
print(ans)