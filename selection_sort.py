import random, time

arr = [i for i in range(10000)]

random.shuffle(arr)
sta = time.time()
s_arr = []

for i in range(len(arr)):
    m = min(arr)
    s_arr.append(m)
    arr.remove(m)         # time taking =  1.537973165512085

print(s_arr)
andt = time.time()
print("time taking = ", andt-sta)
# arr.sort()
# print(arr)
# andt = time.time()
# print("time taking = ", andt-sta)