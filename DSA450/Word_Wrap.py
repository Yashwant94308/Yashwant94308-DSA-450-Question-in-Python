import sys

nums = [6, 6, 7, 4, 4]

k = 9


def solveWordWrap():
    n = len(nums)
    cur_len = nums[0]
    ans = 0

    for i in range(1, n):
        temp = cur_len + nums[i] + 1
        if temp == k and i == n - 1:
            cur_len = temp
        elif temp >= k:
            ans += (k - cur_len)
            cur_len = nums[i]
        else:
            cur_len = temp

    return ans


# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# n = input().decode()
#
# start = time.perf_counter()
# # Output Integer
n = 5
# sys.stdout.write(str(n) + "\n")

# Output String
s = "GeeksforGeeks\n"
sys.stdout.write(s)

# Output Array
arr = [1, 2, 3, 4]
# sys.stdout.write(
#     " ".join(map(str, arr)) + "\n"
# )

# # Stores the end time
# end = time.perf_counter()
#
# # Print the time taken
# print("\nTime taken in Fast Output:", end - start)

print(solveWordWrap())
