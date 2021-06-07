A = [1, 1, 1, 20, 40, 80]
B = [1, 1, 20, 80, ]
C = [1, 1, 15, 20, 1, 70, 80, 120]
# A = [3, 3, 3]
# B = [3, 3, 3]
# C = [3, 3, 3]
n1 = len(A)
n2 = len(B)
n3 = len(C)
common = []
i = 0
j = 0
k = 0
while i < n1 and j < n2 and k < n3:
    if A[i] == B[j] == C[k]:
        if A[i] not in common:
            common.append(A[i])
        i += 1
        j += 1
        k += 1
    elif A[i] < B[j] or A[i] < C[k]:
        i += 1
    elif B[j] < A[i] or B[j] < C[k]:
        j += 1
    elif C[k] < A[i] or C[k] < B[j]:
        k += 1
print(common)
