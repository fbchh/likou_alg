"""
xxx
"""


def solve1(nums1, nums2):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    _ = {}
    for e in nums1:
        _[e] = _.get(e, 0) + 1

    res = []
    for e in nums2:
        if e in nums1:
            res.append(e)

    return res


if __name__ == "__main__":
    print(solve1([1, 2, 2, 1], [2, 2]))
    print(solve1([4, 9, 5], [9, 4, 9, 8, 4]))
    pass
