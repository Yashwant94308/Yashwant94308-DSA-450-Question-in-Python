# YASHWANT KUMAR

if __name__ == '__main__':
    f = True
    while f:

        a = list(map(int, input().split()))
        if a[0] == 0:
            f = False
            break
        b = list(map(int, input().split()))

        n = a.pop(0)
        m = b.pop(0)
        # a.sort()
        # b.sort()

        s1 = 0
        s2 = 0
        ma = 0
        i = 0
        j = 0
        while i < n and j < m:
            if a[i] < b[j]:
                s1 += a[i]
                i += 1
            elif a[i] > b[j]:
                s2 += b[j]
                j += 1
            else:
                ma = ma + max(s1, s2) + a[i]
                s1 = s2 = 0
                i += 1
                j += 1
        while i < n:
            s1 += a[i]
            i += 1
        while j < m:
            s2 += b[j]
            j += 1
        ma = ma + max(s1, s2)

        print(ma)
