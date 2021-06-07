a1 = [11, 1, 13, 21, 3, 7]
a2 = [4]
n = len(a1)
m = len(a2)


def isSubset():
    a1.sort()
    a2.sort()
    i = 0
    j = 0
    while i < n and j < m:
        if a1[i] == a2[j]:
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a1[i] > a2[j]:
            return "No"
    if j < m:
        return 'No'
    else:
        return 'Yes'

print(isSubset())