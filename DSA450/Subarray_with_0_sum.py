arr = [4, 2, -3, 9, 6]


def subArrayExists(arr, n):
    ##Your code here
    # Return true or false
    s = set()
    v = 0
    for i in arr:

        v += i
        if i == 0:
            return True
        elif v == 0:
            return True
        elif v in s:
            return True
        else:
            s.add(v)
    return False


print(subArrayExists(arr, len(arr)))
