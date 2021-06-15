def main():
    li = []
    k = int(input("k: "))
    n = int(input())
    for i in range(n):
        li.append(int(input()))
    pred = [li[0]]

    for i in range(1, n):
        pred.append(pred[i - 1] + li[i])
    if pred[n - 1] < k:
        print(-1)
    else:
        ans = 1e9
        for i in range(n):
            left = i
            r = n

            while left < r:
                mid = (left + r) // 2
                if pred[mid] - pred[i - 1] > k:
                    ans = min(ans, mid - i + 1)
                    r = mid - 1
                else:
                    left = mid + 1
        print(ans)


main()
