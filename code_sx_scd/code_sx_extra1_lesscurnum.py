"""
xxx
"""


def solve(nums):
    inner_nums = sorted(nums)
    inner_hash = {}
    for i, e in enumerate(inner_nums):
        if e not in inner_hash:
            inner_hash[e] = i
    for i, e in enumerate(nums):
        inner_nums[i] = inner_hash[e]

    return inner_nums


if __name__ == "__main__":
    tst_nums = [8, 1, 2, 2, 3]
    print(solve(tst_nums))
