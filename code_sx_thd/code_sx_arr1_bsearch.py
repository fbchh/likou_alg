"""
xxx
"""


def solve(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return - 1


if __name__ == "__main__":
    print(solve([-1, 0, 3, 5, 9, 12], 9))
    print(solve([-1, 0, 3, 5, 9, 12], 2))
    print(solve([5], -5))
    ...
