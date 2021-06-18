def check(sm, a, mid):

    if sm[mid] >= a:
        return True
    if sm[mid] < a:
        return False


def check2(sm, a, mid):

    if sm[mid] <= a:
        return True
    if sm[mid] > a:
        return False


if __name__ == '__main__':
    n, a, b = [int(x) for x in input().split()]

    sm = [0]
    temp = 0
    for i in range(n):
        t = int(input())

        temp += t
        sm.append(temp)

    sm.sort()
    # print(sm)
    lo = 0
    hi = n
    lowe = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(sm, a, mid):

            lowe = mid
            hi = mid - 1
        else:
            lo = mid + 1
    # print(lowe)
    lo = 0
    hi = n
    # print(hi)
    up = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        # print("mud", mid)
        if check2(sm, b, mid):

            up = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(up-lowe+2)
