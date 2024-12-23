"""
xxx
"""


def solve(nums, s):
    nums = [0] + nums
    l = 0
    nums_len = len(nums)
    sum_res = nums[0]
    res_len = nums_len
    for i in range(1, nums_len):
        sum_res += nums[i]
        while sum_res - nums[l] >= s:
            sum_res -= nums[l]
            l += 1
            res_len = min(i - l + 1, res_len)
    return res_len if sum_res >= s else 0


def tst():
    print(solve([2, 3, 1, 2, 4, 3], 7))
    print(solve([1, 2, 3, 4, 5], 15))
    print(solve([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15))
    print(solve([2, 3, 1, 1, 1, 1, 1], 5))


if __name__ == "__main__":
    tst()
    ...
