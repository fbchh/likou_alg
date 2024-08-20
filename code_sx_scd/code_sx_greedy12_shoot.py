"""
xxx
"""


def solve(points):
    _len = len(points)
    if _len <= 1:
        return _len

    points = sorted(points, key=lambda x: (x[0], x[1]))
    shoot_count = 0
    com_range = points[0]
    for i in range(_len):
        if points[i][0] <= com_range[1]:
            com_range = [points[i][0], min(com_range[1], points[i][1])]
        else:
            shoot_count += 1
            com_range = points[i]
    shoot_count += 1
    return shoot_count


if __name__ == "__main__":
    print(solve([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print(solve([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(solve([[1, 2], [2, 3], [3, 4], [4, 5]]))
    ...
