import sys

sys.setrecursionlimit(100000)
li = ['1', '2', '3', '4']

n = len(li)

cnt = [0]


def permu(arr, l, r, ):
    if l == r:
        print(arr, end=" ")
        # cnt[0] += 1
        # print(cnt)

    else:
        for i in range(l, r):
            arr[l], arr[i] = arr[i], arr[l]
            permu(arr, l + 1, r)
            arr[i], arr[l] = arr[l], arr[i]


permu(li, 0, n)
