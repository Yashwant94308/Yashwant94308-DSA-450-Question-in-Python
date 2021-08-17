n, k = map(int,input().split())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
x1 = 0
y1 = 0
x2 = n
y2 = n
a1 = -1
b1 = -1
a2 = -1
b2 = -1
while True:
    su = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            su += arr[i][j]
    if su >= k:
        a1 = x1
        b1 = y1
        a2 = x2
        b2 = y2
        x2 -= 1
        y2 -= 1
    else:
        break
if a1 == -1:
    print('NO')
else:
    print('YES')
    print(a1+1,b1+1,a2,b2)


