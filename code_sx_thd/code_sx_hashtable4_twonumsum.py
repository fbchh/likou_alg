"""
xxx
"""


def solve(nums, target):
    inner_dict = {}

    for i in range(len(nums)):
        inner_dict[target - nums[i]] = i

    for i in range(len(nums)):
        num_idx = inner_dict.get(nums[i], -1)
        if num_idx != -1 and num_idx != i:
            return [num_idx, i]
    return None


def tst():
    print(solve([2, 7, 11, 15], 9))
    print(solve([3, 2, 4], 6))
    print(solve([3, 3], 6))


if __name__ == "__main__":
    tst()
