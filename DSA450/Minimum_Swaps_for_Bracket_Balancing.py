s = "]][["


def swapCount(s):

    pos = []

    for i in range(len(s)):
        if s[i] == '[':
            pos.append(i)

    count = 0

    p = 0

    sum = 0
    s = list(s)

    for i in range(len(s)):

        if s[i] == '[':
            count += 1
            p += 1
        elif s[i] == ']':
            count -= 1

        if count < 0:

            sum += pos[p] - i
            s[i], s[pos[p]] = (s[pos[p]],
                               s[i])
            p += 1

            count = 1
    return sum

print(swapCount(s))