# User function Template for python3
class Solution:
    def nextPermutation(self, N, nums):
        # code here
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def reverse(i):
            j = len(nums) - 1
            while i < j:
                swap(i, j)
                i += 1
                j -= 1

        for i in range(N):
            nums[i] = str(nums[i])

        i, j = len(nums) - 1, len(nums) - 1
        while i > 0 and int(nums[i - 1]) >= int(nums[i]):     i -= 1

        if i > 0:
            while j >= 0 and int(nums[j]) <= int(nums[i - 1]):    j -= 1
            swap(i - 1, j)

        reverse(i)
        for i in range(N):
            nums[i] = int(nums[i])
        return nums


# {
# Driver Code Starts
# Initial Template for python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i], end=" ")
        print()
# } Driver Code End
