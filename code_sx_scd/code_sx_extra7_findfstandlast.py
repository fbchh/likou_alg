"""
xxx
"""


def solve(nums, target):
    start = 0
    last = len(nums) - 1
    l = start
    r = last

    res_l = float("inf")
    res_r = -1
    while l <= last and r >= start:
        if nums[l] == target:
            res_l = min(res_l, l)

        if nums[r] == target:
            res_r = max(res_r, r)

        l += 1
        r -= 1

    if res_r == -1:
        return -1, -1
    return res_l, res_r


if __name__ == "__main__":
    print(solve([5, 7, 7, 8, 8, 10], 8))
    print(solve([5, 7, 7, 8, 8, 10], 6))
    print(solve([], 0))
    ...
