"""
xxx
"""


def solve(intervals):
    _len = len(intervals)
    if _len <= 1:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    res = [intervals[0]]

    for i in range(1, _len):
        if intervals[i][0] == res[-1][0]:
            res[-1] = [res[-1][0], min(res[-1][1], intervals[i][1])]
        elif res[-1][0] < intervals[i][0] < res[-1][1]:
            if intervals[i][1] <= res[-1][1]:
                res[-1] = intervals[i]
            continue
        elif intervals[i][0] >= res[-1][1]:
            res.append(intervals[i])

    return _len - len(res)


def solve1(intervals):
    # 逻辑简化
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    count = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])  # 更新重叠区间的右边界
            count += 1

    return count


if __name__ == "__main__":
    print(solve([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(solve([[1, 2], [1, 2], [1, 2]]))
    print(solve([[1, 2], [2, 3]]))
    ...
