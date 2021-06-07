arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]  # ans =4
x = 280


def sb():
    if arr[0] >= x:
        return 1
    ans = 1000000
    check = arr[0]
    left = 0
    i = 1
    li = []
    while len(arr) > i > left:

        if arr[i] >= x:
            return 1
        elif check < x:
            check += arr[i]
            li.append(arr[i])

            i += 1
        elif check > x:
            check = sum(arr[left:])

            ans = min(ans, i - left)
            left += 1
            print(ans)
    return ans


print(sb())
