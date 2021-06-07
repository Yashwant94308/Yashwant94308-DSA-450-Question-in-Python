s = ['foo', 'bar', 'baz']



def s_s():
    ans = []
    for i in s:
        k = list(i)
        t = k.copy()
        k.sort()

        if t == k:
            ans.append("No")
        else:
            ans.append("yes")
    return ans


result = s_s()

print(result)