arr = [2,5,-3,9,-1,45,-46]
print(arr)
# using linear search
for i in range(len(arr)):
	if arr[i] < 0:
		key = arr[i]
		arr.remove(key)
		arr.insert(0, key)
print(arr)