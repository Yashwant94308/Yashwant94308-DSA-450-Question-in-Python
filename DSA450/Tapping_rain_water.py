arr = [3, 0, 0, 2, 4]
n = len(arr)


def trappingWater():
    result = 0

    left_max = 0
    right_max = 0

    lo = 0
    hi = n - 1

    while (lo <= hi):

        if (arr[lo] < arr[hi]):

            if (arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if arr[hi] > right_max:
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result


print(trappingWater())
