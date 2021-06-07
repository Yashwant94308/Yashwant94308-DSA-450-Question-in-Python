import math

arr1 = [1, 2, 11, 4, 5]
arr2 = [2, 7, 9, 10]


def nextGap(g):
    if g <= 1:
        return 0
    return math.ceil(g / 2)


n = gap = len(arr1) + len(arr2)
gap = nextGap(gap)
while gap > 0:
    i = 0
    while i + gap < n:
        if arr1[i] > arr1[i + gap]:
            arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]

        i += 1
    gap = nextGap(gap)
print(arr1+arr2)

