def im_possible(arr, n, m, min_s):
    n_st = 1
    c_s = 0
    for i in range(n):
        if arr[i] > min_s:
            return False
        if arr[i] + c_s > min_s:
            n_st += 1
            c_s = arr[i]
            if n_st > m:
                return False
        else:
            c_s += arr[i]
    return True


def fp(arr, n, m):
    if m > n:
        return -1
    ans = 1e9
    s = 0
    for i in range(n):
        s += arr[i]
    end, start = s, 0
    while start <= end:
        mid = (start + end) // 2
        if im_possible(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans


n = 4
arr = [12, 34, 67, 90]
m = 2
print(fp(arr, n, m))
