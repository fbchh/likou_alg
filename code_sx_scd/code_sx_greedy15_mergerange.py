"""
xxx
"""


def solve(intervals):
    _len = len(intervals)
    if _len <= 1:
        return intervals
    intervals.sort(key=lambda x: (x[0], x[1]))

    res = [intervals[0]]
    for i in range(1, _len):
        if intervals[i][0] <= res[-1][1]:
            res[-1] = [res[-1][0], max(intervals[i][1], res[-1][1])]
        else:
            res.append(intervals[i])

    return res


if __name__ == "__main__":
    print(solve([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solve([[1, 4], [4, 5]]))
    ...
