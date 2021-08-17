n = 3
start = [10, 12, 20]
end = [20, 25, 30]

# def dfs(index, st, e, cnt):
#     if index == n:
#         ans[0] = max(ans[0], cnt)
#         return
#     if start[index] >= e:
#         dfs(index + 1, start[index], end[index], cnt + 1)
#         dfs(index + 1, st, e, cnt)
#     else:
#         dfs(index + 1, st, e, cnt)


# dfs(0, 0, 0, 0)
arr = []
for i in range(3):
    arr.append([start[i], end[i]])
arr.sort(key=lambda x: x[1])
cnt = 1
i = 0

for j in range(1, n):
    if arr[i][1] < arr[j][0]:
        cnt += 1
        i = j
print(cnt)

