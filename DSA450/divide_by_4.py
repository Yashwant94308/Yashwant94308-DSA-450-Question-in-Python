arr = [20, 16, 11, 16, 14]
# arr = [2, 2, 1, 7, 5]
n = len(arr)
k = 4
hm = {0:0}
cnt = 0
for i in range(n):
    r = arr[i] % k
    if (k - r) in hm:
        cnt += hm[k - r]
    if r in hm:
        hm[r] += 1
    else:
        hm[r] = 1
cnt += hm[0] * (hm[0] - 1) / 2
print(cnt)

# hm = [0] * k
# for i in range(n):
#     hm[arr[i] % k] += 1
# s = hm[0] * (hm[0] - 1) / 2
# i = 1
# while i <= k // 2 and i != (k - i):
#     s += hm[i] * hm[k-i]
#     i += 1
# if k % 2 == 0:
#     s += hm[k // 2] * (hm[k // 2] - 1) / 2
# print(s)
