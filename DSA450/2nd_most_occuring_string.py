from collections import Counter as ctr

arr = ['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']


def sol():

    cnt = ctr(arr)
    j = ''
    m = max(cnt.values())
    for k, v in cnt.items():
        if v == m:
            j = k
            break
    cnt.pop(j)
    m = max(cnt.values())
    for k, v in cnt.items():
        if v == m:
            return k


print(sol())
