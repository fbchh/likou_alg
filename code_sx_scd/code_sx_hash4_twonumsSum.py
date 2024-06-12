"""
xxx
"""


def solve1(nums, target):
    if len(nums) < 2:
        return None
    _ = {}
    for i in range(len(nums)):
        other_num = target - nums[i]
        if other_num in _:
            return _[other_num], i
        else:
            _[nums[i]] = i


if __name__ == "__main__":
    tst_ege1_nums = [2, 7, 11, 15]
    print(solve1(tst_ege1_nums, 9))

    tst_ege2_nums = [3, 2, 3]
    print(solve1(tst_ege2_nums, 6))

    print(solve1([3, 3], 6))
    pass
