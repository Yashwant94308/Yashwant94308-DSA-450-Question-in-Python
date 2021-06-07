import random, time

num = [i for i in range(1000000)]
# making list time 0.10934901237487793 for loop

# making list time 0.04686570167541504 for loop inside lsit


random.shuffle(num)

# print(min(num))  # taking time for min max function 0.10933327674865723
# print(max(num))
st = time.time()
mini = maxi = num[0]

for i in num:  # time taking by for loops to find min and max 0.2811875343322754
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i
print("max = ", maxi)

print('min = ', mini)
end = time.time()
print("time taking by for loops to find min and max", end - st)
