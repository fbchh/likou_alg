"""
xxx
"""


def solve1(nums1, nums2, nums3, nums4):  # 从整体上解决比较困难，可以把问题拆解，化整为零
    _map = {}
    for e1 in nums3:
        for e2 in nums4:
            _ = e1 + e2
            _map[_] = _map.get(_, 0) + 1

    _res = 0
    for e1 in nums1:
        for e2 in nums2:
            _ = e1 + e2
            if -_ in _map:
                _res += _map[-_]
    return _res


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(solve1(A, B, C, D))

    A = [-1, -1]
    B = [-1, 1]
    C = [-1, 1]
    D = [1, -1]
    print(solve1(A, B, C, D))
    pass
