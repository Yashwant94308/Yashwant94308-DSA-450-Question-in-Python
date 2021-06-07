arrs = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]


class Solution:

    def inversionCount(self, arr, n):
        # Your Code Here
        def mergAndCountInversion(arr, temp_arr, left, right):
            inv_cnt = 0
            if left < right:
                mid = (left + right) // 2
                inv_cnt += mergAndCountInversion(arr, temp_arr, left, mid)
                inv_cnt += mergAndCountInversion(arr, temp_arr, mid + 1, right)
                inv_cnt += mergeArray(arr, temp_arr, left, mid, right)
            return inv_cnt

        def mergeArray(arr, temp_arr, left, mid, right):
            inv_cnt = 0
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp_arr[k] = arr[i]
                    i += 1
                    k += 1
                else:
                    temp_arr[k] = arr[j]
                    inv_cnt += (mid - i) + 1
                    k += 1
                    j += 1
            while i <= mid:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            while j <= right:
                temp_arr[k] = arr[j]
                k += 1
                j += 1
            for loop_var in range(left, right + 1):
                arr[loop_var] = temp_arr[loop_var]
            return inv_cnt

        temp_arr = [0] * n
        return mergAndCountInversion(arr, temp_arr, 0, n - 1)


s = Solution()
print(s.inversionCount(arrs, len(arrs)))

