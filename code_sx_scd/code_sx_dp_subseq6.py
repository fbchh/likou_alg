"""
xxx
"""


def solve(nums):
    # 动规解法
    len_nums = len(nums)

    res = [0] * len_nums
    res[0] = nums[0]

    for i in range(1, len_nums):
        res[i] = nums[i] if res[i - 1] < 0 else res[i - 1] + nums[i]

    return max(res)


def solve1(nums):
    # 贪心解法
    last_count = nums[0]
    cur_count = nums[0]
    for i in range(1, len(nums)):
        if cur_count < 0:
            cur_count = nums[i]
        else:
            cur_count += nums[i]
        last_count = max(cur_count, last_count)
    return last_count


if __name__ == "__main__":
    # print(solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(solve([1]))
    # print(solve([5, 4, -1, 7, 8]))

    print(solve1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solve1([1]))
    print(solve1([5, 4, -1, 7, 8]))
    ...
