import random, time

num = [i for i in range(1000000)]
# making list time 0.10934901237487793 for loop

# making list time 0.04686570167541504 for loop inside lsit


random.shuffle(num)
num.sort()

print(num[-5])