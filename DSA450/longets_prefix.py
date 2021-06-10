strs = ["dog","racecar","car"]


def slo():
    strs.sort()
    n = len(strs[0])

    for j in range(1, len(strs)):
        i = 0
        while i < n:
            if strs[0][i] == strs[j][i]:
                i += 1
            else:
                break
        n = i
    if n > 0:
        return '"' + strs[0][:n] + '"'
    else:
        return '""'

print(slo())

