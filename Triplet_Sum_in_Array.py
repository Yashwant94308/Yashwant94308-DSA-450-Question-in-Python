# arr = [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424,
#        130, 230, 566, 560, 933]
A = [23, 42, 113, 130, 217, 230, 272, 338, 358, 358, 362, 424, 527, 557, 560, 566,
       586, 618, 627, 697, 718, 870, 897, 933]
sum = 986
arr_size = len(A)


def find3Numbers():
    for i in range(arr_size - 1):
        s = set()
        c = sum - A[i]
        for j in range(i + 1, arr_size):
            if c - A[j] in s:
                return True
            s.add(A[j])
    return False


print(find3Numbers())
