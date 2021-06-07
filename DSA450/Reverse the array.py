a = []
for i in range(1101):
    a.append(i)
# print(a)
# print(a[::-1])  # 1
# print(list(reversed(a))) # 2
#
# b = 'abc'
# print(b[::-1])
import time
st = time.time()
print(list(reversed(a)))
end = time.time()
print('\nfor loop', end-st)


# for loop execution time = 0.01562190055847168 for 1100 round
# list slicing execution time=0.015642881393432617 for 1100 round
# reversed function execution time = 0.015619754791259766 for 1100 round

