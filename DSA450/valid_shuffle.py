first = "XY"
second = "12"
results = ["1XY2", "Y12X"]


def vd(result):
    if len(result) != len(first) + len(second):
        return False
    i = 0
    j = 0
    k = 0
    while k < len(result):
        if i < len(first) and first[i] == result[k]:
            i += 1
            k += 1
        elif j < len(second) and second[j] == result[k]:
            j += 1
            k += 1
        else:
            return False
    if i < len(first) or j < len(second):
        return False
    else:
        return True


for m in results:
    print(vd(m))
