arr1 = [5, 6, 7]
arr2 = [1, 2, 3, 4, 5]
def bin(a, arr, lo, hi):
	
	if lo < hi:
		mid = lo + (hi - lo)  // 2
		
		if arr[mid] == a:
			return mid
		elif arr[mid]< a:
			return bin(a, arr, mid+1, hi)
		else:
			return bin(a, arr, lo, mid-1)
	else: 
		return -1
count = 0
for i in range(len(arr1)):
	lo = 0
	hi = len(arr2)
	re = bin(arr1[i], arr2, lo, hi)
	
	if re != -1:
		count += 1

print(count)


 