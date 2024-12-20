"""
xxx
"""


def solve(nums, val):
    nums_len = len(nums)
    fast_idx = -1
    for i in range(nums_len):
        if nums[i] == val:
            fast_idx = i + 1 if fast_idx == -1 else fast_idx + 1
            while fast_idx < nums_len:
                if nums[fast_idx] != val:
                    _ = nums[fast_idx]
                    nums[fast_idx] = nums[i]
                    nums[i] = _
                    break
                fast_idx += 1

    for i in range(nums_len):
        if nums[i] == val:
            return i


def solve1(nums, val):
    slow = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[slow] = nums[i]
            slow += 1
    return slow


if __name__ == "__main__":
    print(solve1([3, 2, 2, 3], 3))
    print(solve1([0, 1, 2, 2, 3, 0, 4, 2], 2))
    ...
