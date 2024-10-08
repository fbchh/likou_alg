"""
xxx
"""


def solve(nums):
    def inner_solve(tgt_nums):
        inner_len_nums = len(tgt_nums)
        res = [0] * inner_len_nums
        res[0] = tgt_nums[0]
        res[1] = max(tgt_nums[:2])

        for i in range(2, inner_len_nums):
            res[i] = max(res[i - 2] + tgt_nums[i], res[i - 1])

        return res[-1]

    len_nums = len(nums)
    if len_nums == 0:
        return 0
    if len_nums <= 2:
        return max(nums)
    res_res = inner_solve(nums[:-1]), inner_solve(nums[1:])
    return max(res_res)


if __name__ == "__main__":
    print(solve([2, 3, 2]))
    print(solve([1, 2, 3, 1]))
    print(solve([1, 2, 3]))
    print(solve([1]))
    ...
