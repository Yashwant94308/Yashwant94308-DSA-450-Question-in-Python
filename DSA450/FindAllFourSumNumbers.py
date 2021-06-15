class Solution:
    def fourSum(self, arr, K):
        # code here
        n = len(arr)
        li = []

        arr.sort()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1
                while l < r:
                    if arr[i] + arr[j] + arr[l] + arr[r] == k:
                        temp = [arr[i], arr[j], arr[l], arr[r]]
                        temp.sort()
                        if temp not in li:
                            li.append(temp)
                        l += 1
                        r -= 1
                    elif arr[i] + arr[j] + arr[l] + arr[r] < k:
                        l += 1
                    else:
                        r -= 1
        li.sort()
        return li
