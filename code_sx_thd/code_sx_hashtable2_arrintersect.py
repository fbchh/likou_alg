"""
xxx
"""


def solve(nums1, nums2):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))

    inner_dict = {}
    for e in nums1:
        sgl_num = inner_dict.get(e, 0)
        if sgl_num == 0:
            inner_dict[e] = 1
    res = []
    for e in nums2:
        sgl_num = inner_dict.get(e, 0)
        if sgl_num == 1:
            res.append(e)
    return res


if __name__ == "__main__":
    ...
