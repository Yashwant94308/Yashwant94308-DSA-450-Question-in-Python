# Roti Pratha
def check(p, labour, li, mid):
    pratha = 0
    time = 0
    for i in range(labour):
        time = li[i]
        j = 2
        while time <= mid:
            pratha += 1
            time = time + (li[i] * j)
            j += 1
        if pratha >= p:
            return True
    return False


if __name__ == '__main__':

    t = int(input())
    while t > 0:
        p = int(input())
        li = list(map(int, input().split()))
        labour = li.pop(0)
        # print(labour, li)
        lo = 0
        hi = 1e4
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(mid)
            if check(p, labour, li, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        print(int(ans))

        t -= 1
