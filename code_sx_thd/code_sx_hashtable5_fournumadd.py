"""
xxx
"""


def solve(nums1, nums2, nums3, nums4):
    inner_dict = {}
    for e in nums1:
        for e1 in nums2:
            sgl_add_res = e + e1
            inner_dict[sgl_add_res] = inner_dict.get(sgl_add_res, 0) + 1

    res = 0
    for e in nums3:
        for e1 in nums4:
            sgl_add_res = -(e + e1)
            sgl_dict_res = inner_dict.get(sgl_add_res, 0)
            if sgl_dict_res != 0:
                res += sgl_dict_res
    return res


def tst():
    print(solve([1, 2], [-2, -1], [-1, 2], [0, 2]))
    print(solve([-1, -1], [-1, 1], [-1, 1], [1, -1]))


if __name__ == "__main__":
    tst()
