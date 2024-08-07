"""
xxx
"""


def solve(nums):
    _len = len(nums)
    if _len == 1:
        return nums[0]

    res = -9999
    count = 0
    for i in range(_len):
        count += nums[i]
        if count > res:
            res = count

        if count < 0:
            count = 0

    return res


if __name__ == "__main__":
    tst_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solve(tst_nums))
    ...
