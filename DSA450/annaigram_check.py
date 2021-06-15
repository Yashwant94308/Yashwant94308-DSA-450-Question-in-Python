from collections import defaultdict

word = ['act','god','cat','dog','tac']


def sol():
    v = word.copy()
    a = defaultdict()
    for i in range(len(word)):
        t = ''
        for o in sorted(v[i]):
            t += o
        if len(a) == 0:

            a[t] = [i]
        elif t in a.keys():
            a[t].append(i)
        else:
            a[t] = [i]
    li = []
    for i in a.values():
        temp = []
        for j in i:
            t = word[j]
            temp.append(t)
        li.append( temp)

    return li


ans = sol()
for grp in sorted(ans):
    for word in grp:
        print(word, end=' ')
    print()
