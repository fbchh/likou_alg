"""
xxx
"""


def solve(nums):
    sum_nums = sum(nums)

    backpack_max_num = sum_nums / 2
    if backpack_max_num != int(backpack_max_num):
        return False

    # 初始化
    backpack_max_num = int(backpack_max_num)
    res = [0 for _i in range(backpack_max_num + 1)]
    for i in range(backpack_max_num + 1):   
        if i >= nums[0]:
            res[i] = nums[0]

    if res[-1] == backpack_max_num:
        return True

    for i in range(1, len(nums)):
        for j in range(len(res) - 1, 0, -1):
            if j >= nums[i]:
                res[j] = max(nums[i] + res[j - nums[i]], res[j])

        if res[-1] == backpack_max_num:
            return True

    return False


if __name__ == "__main__":
    print(solve([1, 5, 5, 11]))
    print(solve([1, 2, 3, 5]))
    print(solve([1, 2, 5]))
    ...
