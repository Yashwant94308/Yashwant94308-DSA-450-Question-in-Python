import sys

arr = [ [1, 5], [2, 5] ]
brr = [ [1, 5], [2, 5] ]
targetrr = 11


def sol(a, b, target):
    a = sorted(a, key=lambda x: x[1])
    b = sorted(b, key=lambda x: x[1])
    left = 0
    right = len(b) - 1
    curr = -sys.maxsize
    res = []
    while left < len(a) and right >= 0:
        cs = a[left][1] + b[right][1]
        if cs > target:
            right -= 1
        else:
            if cs >= curr:
                if cs > curr:
                    res = []
                    curr = cs
                res.append([a[left][0], b[right][0]])
                count = right
                while count > 0 and b[count][1] == b[count-1][1]:
                    res.append([a[left][0], b[count-1][0]])
                    count -= 1
            left += 1
    if not res:
        res = [[]]
    return res
            
print(sol(arr, brr, targetrr))            
