"""
xxx
"""


def solve(nums):  # 这里没有要求记录最长连续序列的“序列本列”改用计数更好
    res = [nums[0]]
    last_len = 1

    for i in range(1, len(nums)):
        if nums[i] > res[-1]:
            res.append(nums[i])
        else:
            last_len = max(len(res), last_len)
            res = [nums[i]]

    last_len = max(len(res), last_len)
    return last_len


def solve1(nums):  # 动规
    len_nums = len(nums)
    res = [1] * len_nums

    for i in range(1, len_nums):
        if nums[i] > nums[i - 1]:
            res[i] = res[i - 1] + 1

    return max(res)


if __name__ == "__main__":
    # print(solve([1, 3, 5, 4, 7]))
    # print(solve([2, 2, 2, 2, 2]))
    # print(solve([1, 3, 5, 7]))

    print(solve1([1, 3, 5, 4, 7]))
    print(solve1([2, 2, 2, 2, 2]))
    print(solve1([1, 3, 5, 7]))
    ...
