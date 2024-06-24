"""
xxx
"""


def solve1(nums, val):
    p1 = 0
    for p2 in range(len(nums)):
        if nums[p2] != val:
            nums[p1] = nums[p2]
            p1 += 1
    return p1


if __name__ == "__main__":
    print(solve1([3, 2, 2, 3], 3))
    print(solve1([3, 3], 3))
    pass
