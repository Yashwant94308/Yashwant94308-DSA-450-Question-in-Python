arr2 = [0,1,1,1,2,3,6,7,8,9]
# k = 4
x2 = 11




def sol(arr, k, x):
    hm = {}
    for i in range(len(arr)):
        hm[i] = abs(arr[i] - x)
    hm = sorted(hm.items(), key=lambda o: o[1])
    res = []
    i = 1
    for key, v in hm:

        if i > k:
            break

        res.append(arr[key])
        i += 1
    res.sort()
    return res


print(sol(arr2, 9, 4))
