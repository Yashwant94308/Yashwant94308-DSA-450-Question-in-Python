arr = [2, 30, 15, 110, 8, 125, 9, 80]
n = len(arr)


def maxProfit():
    profit = [0] * n
    max_price = arr[n - 1]
    for i in range(n - 2, 0, -1):
        if arr[i] > max_price:
            max_price = arr[i]

        profit[i] = max(profit[i + 1], max_price - arr[i])
    min_price = arr[0]
    for i in range(1, n):
        if min_price > arr[i]:
            min_price = arr[i]

        profit[i] = max(profit[i - 1], profit[i] + (arr[i] - min_price))

    return profit[n - 1]


print(maxProfit())
