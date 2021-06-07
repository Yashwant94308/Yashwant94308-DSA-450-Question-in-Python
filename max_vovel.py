s = 'qwadftteeytaa'
k = 5


def maxVowels():
    prefix_count = [0]
    postfix_count = [0]
    data = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(s)):
        if s[i] in data:
            prefix_count.append(prefix_count[-1] + 1)
        else:
            prefix_count.append(prefix_count[-1])
    res = 0
    print(prefix_count)
    j = 0
    for i in range(k - 1, len(s)):
        
        res = max(res, prefix_count[i + 1] - prefix_count[j])

        j += 1
    return res


print(maxVowels())
