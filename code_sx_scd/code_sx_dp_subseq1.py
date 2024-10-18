"""
xxx
"""


def solve(nums):
    len_nums = len(nums)
    res = 1

    dp = [1] * len_nums
    for i in range(1, len_nums):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])

    return res


if __name__ == "__main__":
    print(solve([10, 9, 2, 5, 3, 7, 101, 18]))
    print(solve([0, 1, 0, 3, 2, 3]))
    print(solve([7, 7, 7, 7, 7, 7, 7]))
    ...
