b = '01111000010'


def cnt_binary():
    cnt = 0
    cnt0 = 0
    cnt1 = 0
    for i in b:
        if i == '0':
            cnt0 += 1
        elif i == '1':
            cnt1 += 1
        if cnt1 == cnt0:
            cnt += 1
    if cnt1 != cnt0:
        return -1
    return cnt

print(cnt_binary())
