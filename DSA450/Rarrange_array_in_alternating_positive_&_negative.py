def Rearrange(arr, n):
    arr2 = arr.copy()
    i = 0
    j = 0
    c = []
    while i < n and j < n:
        if arr[i] < 0 and arr[j] > 0:
            c.append(arr[i])
            c.append(arr[j])
            arr2.remove(arr[i])
            arr2.remove(arr[j])
            i += 1
            j += 1
        else:
            if arr[i] >= 0:
                i += 1
            elif arr[j] < 0:
                j += 1

    for i in arr2:
        c.append(i)
    print(c)


if __name__ == '__main__':
    arrs = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    ns = len(arrs)
    Rearrange(arrs, ns)
