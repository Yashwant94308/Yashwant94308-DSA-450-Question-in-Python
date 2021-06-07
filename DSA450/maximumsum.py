N = 4
arr = [1,2,3,-2,5]
first = arr[0]
f = first
for i in range(1,len(arr)):
	sec = f+ arr[i]
	first = max(first, sec) 
	f = sec
print(first)