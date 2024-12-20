"""
xxx
"""


def solve(nums):
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)
    nums.sort()
    return nums


if __name__ == "__main__":
    ...
