def swap(i, j):
    arr[i] = arr[j] ^ arr[i]
    arr[j] = arr[j] ^ arr[i]
    arr[i] = arr[j] ^ arr[i]


def reverse(i):
    j = N - 1
    while i < j:
        swap(i, j)
        j -= 1
        i += 1


def nextPermutation(n, arr):
    i = n - 1
    j = n - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i > 0:
        while j > 0 and arr[i - 1] >= arr[j]:
            j -= 1
        swap(i - 1, j)
    reverse(i)


t = int(input())
for _ in range(t):
    N = int(input())
    arr = input().split()
    for i in range(N):
        arr[i] = int(arr[i])

    print('Before', arr)

    nextPermutation(N, arr)
    print(arr)
    print()
# } Driver Code End
