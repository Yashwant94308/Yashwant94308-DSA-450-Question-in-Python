digits = '23456789'
n = len(digits)


def solve():
    table = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    q = []
    res = []
    q.append('')
    while len(q) > 0:
        s = q.pop(0)
        if len(s) == n:
            res.append(s)
        else:
            for length in table[int(digits[len(s)])]:
                q.append(s+length)
    return res
print(solve())