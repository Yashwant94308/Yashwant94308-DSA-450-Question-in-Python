import random, time

arr = [i for i in range(10000)]

random.shuffle(arr)
sta = time.time()

for i in range(len(arr)):

    for j in range(0, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:  # time taking in bubble sort:  11.139550685882568

            arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr.sort()

# time taking in inbuilt sort:  0.01606273651123047
print(arr)

enda = time.time()
print('time taking in inbuilt sort: ', enda - sta)
