"""
xxx
"""


def solve(nums, target):
    res = [0] * (target + 1)
    res[0] = 1

    for i in range(target + 1):
        for num in nums:
            if i >= num:
                res[i] += res[i - num]

    return res[-1]


if __name__ == "__main__":
    print(solve([1, 2, 3], 4))
    print(solve([9], 3))
    ...
