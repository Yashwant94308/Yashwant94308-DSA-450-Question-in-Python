S = '1001010'
Q = [[0, 4], [0, 5]]

print('\nnaive Approach -- > Time Complex O(N*M) \n')

# naive Approach Time Complex O(N*M)
for q in Q:
    total = 0
    count = 0
    for i in range(q[0], q[1] + 1):
        if S[i] == '1':
            count = total
        elif S[i] == '0':
            total += 1
    print(count)

print("\nEfficient approach -- > Time complex O(M+N) \n")

# Efficient approach -- > Time complex O(M+N)

left = [0] * (len(S))
right = [0] * len(S)

total = 0
count = 0

for i in range(len(S)):
    if S[i] == '1':
        count = total
    elif S[i] == '0':
        total += 1
    right[i] = count


total = 0
count = 0
for i in range(len(S)-1, -1, -1):

    if S[i] == '1':
        count = total
    elif S[i] == '0':
        total += 1
    left[i] = count

for i in range(len(Q)):
    l = Q[i][0]
    r = Q[i][1]
    print(left[l] + right[r] - total)



