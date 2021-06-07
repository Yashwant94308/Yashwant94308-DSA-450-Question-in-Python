from math import floor

arr = [56, 67, 30, 79]


class Solution:
    def find_median(self, v):
        # Code here
        v.sort()
        n = len(v)
        print(v)

        if n % 2 == 0:
            i = n // 2
            j = i - 1
            r = floor((v[i] + v[j]) / 2)
            print(r)
            return r
        else:
            i = n // 2

            return v[i]


s = Solution()
print(s.find_median(arr))
