"""
xxx
"""


def solve(nums, val):
    num_len = len(nums)
    for i in range(num_len):
        if nums[i] == val:
            l = i + 1
            while l < num_len:
                if nums[l] != val:
                    nums[i] = nums[l]
                    nums[l] = val
                    break
                l += 1
    r = num_len - 1
    while r >= 0 and nums[r] == val:
        r -= 1
    return r + 1


def solve1(nums, val):
    nums_len = len(nums)
    f = 0
    s = 0
    while f < nums_len:
        if nums[f] != val:
            nums[s] = nums[f]
            s += 1
        f += 1
    return s


def tst():
    print(solve([3, 2, 2, 3], 3))
    print(solve([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(solve([1], 1))

    print(solve1([3, 2, 2, 3], 3))
    print(solve1([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(solve1([1], 1))


if __name__ == "__main__":
    tst()
