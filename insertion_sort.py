import random, time

arr = [i for i in range(10000)]

random.shuffle(arr)
sta = time.time()

# for i in range(1, len(arr)):
#     j = i - 1
#     key = arr[i]
#     while j >= 0 and arr[j] > key:        # time taking in insertion sort:  6.307011604309082
#         arr[j + 1] = arr[j]
#
#         j -= 1
#     arr[j + 1] = key
arr.sort()          # time taking in inbuilt sort:  0.013187408447265625

print(arr)

enda = time.time()
print("time taking in inbuilt sort: ", enda-sta)
