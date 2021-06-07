prices = [7, 6, 3, 4, 7, 1]


def maxProfit():
    maxi = 0
    ans = 0
    mini = max(prices)
    for i in prices:
        if i < mini:
            mini = i
            maxi = 0
        elif i > maxi:
            maxi = i
        ans = max(ans, maxi - mini)
    return ans


print(maxProfit())
