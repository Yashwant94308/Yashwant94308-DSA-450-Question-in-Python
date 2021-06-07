B = ['f', 'mes', 'ckjcaz', 'dr', 'dg', 'rqscczy']
A = "mesckjcazdgfckjcazckjcazmesckjcaz"


def wb():
    n = len(B)
    ans = 0
    i = 0
    j = 0
    while i < len(A) and j < n:
        if A[i] in B[j]:

            o = i
            k = 0
            while k < len(B[j]):
                if B[j][k] == A[o]:
                    o += 1
                    k += 1

                    if o >= len(A):
                        break
                else:

                    break

            if k >= len(B[j]):
                i = o
                j = 0
                ans = 1
            else:
                j += 1
                ans = 0

        else:
            j += 1
            ans = 0
    return ans


print(wb())
