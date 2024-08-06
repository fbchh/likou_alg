"""
xxx
"""


def solve(nums):
    _len = len(nums)
    if _len < 0:
        return None

    res = 1
    pre_diff = 0
    for i in range(len(nums) - 1):
        cur_diff = nums[i + 1] - nums[i]
        if (pre_diff >= 0 > cur_diff) or (pre_diff <= 0 < cur_diff):
            res += 1
            pre_diff = cur_diff

    return res


if __name__ == "__main__":
    tst_ege_nums = [1, 7, 4, 9, 2, 5]
    print(solve(tst_ege_nums))
    print(solve([0, 0]))
    ...
