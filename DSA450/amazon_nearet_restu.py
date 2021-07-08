import math
location = [[1, 2], [3, 4], [1, -1]]
X = 2
# res = []
# for i in range(len(location)):
#     res.append([location[i][0], location[i][1], math.sqrt((location[i][1]**2)+(location[i][1]**2))])
# res = sorted(res, key=lambda x: x[2])
# ans = []
# for i in res:
#     ans.append([i[0], i[1]])
# print(ans[:X])

location = sorted(location, key=lambda x: x[0]**2 + x[1]**2)
print(location[:X])
