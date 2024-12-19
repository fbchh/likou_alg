"""
xxx
"""


def solve(nums):
    nums_tol = sum(nums)
    l = 0
    r = nums_tol

    for i in range(len(nums)):
        r -= nums[i]
        if l == r:
            return i
        l += nums[i]

    return -1


if __name__ == "__main__":
    print(solve([1, 7, 3, 6, 5, 6]))
    print(solve([1, 2, 3]))
    print(solve([2, 1, -1]))
    ...
