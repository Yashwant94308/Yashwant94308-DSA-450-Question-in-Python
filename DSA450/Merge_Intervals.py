# intervals = [[1, 4], [2, 3], [3, 5], [9, 12], [10, 11], [10, 14], [20, 23]]
intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]


def MergeIntervals():
    if intervals is None or len(intervals) == 0:
        return 0
    intervals.sort()
    mergeIntervals = [intervals[0]]
    for i in range(1, len(intervals)):
        x1 = intervals[i][0]
        x2 = intervals[i][1]
        y1 = mergeIntervals[len(mergeIntervals) - 1][0]
        y2 = mergeIntervals[len(mergeIntervals) - 1][1]

        if y2 >= x1:

            mergeIntervals[len(mergeIntervals) - 1][1] = max(x2, y2)
            mergeIntervals[len(mergeIntervals) - 1][0] = min(x1, y1)
        else:
            mergeIntervals.append(intervals[i])

    return mergeIntervals


print(MergeIntervals())

# index = []
#     val = []
#     for i in range(0, len(repeatedIntervals)):
#         mergeIntervals.append(repeatedIntervals[i])
#     for i in range(0, len(intervals)):
#         mergeIntervals.append(intervals[i])
#     for i in range(0, len(mergeIntervals)):
#         for j in range(i+1, len(mergeIntervals)):
#             if mergeIntervals[i][1] >= mergeIntervals[j][1] and mergeIntervals[i][0] <= mergeIntervals[j][0]:
#                 index.append(j)
#     for i in set(index):
#         val.append(mergeIntervals[i])
#     for i in val:
#         mergeIntervals.remove(i)
#
#     return mergeIntervals
