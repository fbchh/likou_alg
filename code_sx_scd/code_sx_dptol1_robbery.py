"""
xxx
"""


def solve1(nums):
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    if len_nums <= 2:
        return max(nums)

    res = [0] * len_nums
    res[0] = nums[0]
    res[1] = max(nums[: 2])

    for i in range(2, len_nums):
        res[i] = max(res[i - 2] + nums[i], res[i - 1])

    return res[-1]


if __name__ == "__main__":
    print(solve1([1, 2, 3, 1]))
    print(solve1([2, 7, 9, 3, 1]))
    ...
