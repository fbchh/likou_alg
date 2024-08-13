"""
xxx
"""


def solve(nums, k):
    nums.sort()
    idx = -1
    for i in range(len(nums)):
        if nums[i] <= 0 < k:  # 第一次贪心 先把绝对值最大的负值转为正值
            nums[i] = - nums[i]
            k -= 1
            idx += 1
        else:
            break

    idx = max(0, idx)
    if idx < len(nums) - 1 and nums[idx + 1] < nums[idx]:
        idx += 1
    while k > 0:
        nums[idx] = -nums[idx]  # 第二次贪心 把最小的数值反复反转
        k -= 1

    return sum(nums)


if __name__ == "__main__":
    print(solve([4, 2, 3], 1))
    print(solve([2, -3, -1, 5, -4], 2))
    print(solve([8, -7, -3, -9, 1, 9, -6, -9, 3], 8))
    ...
