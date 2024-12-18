"""
xxx
"""


def solve(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            new_idx = i
            while new_idx < len(nums):
                if nums[new_idx] != 0:
                    nums[i] = nums[new_idx]
                    nums[new_idx] = 0
                    break
                new_idx += 1
    return nums


def solve1(nums):
    """
    在以上的基础上添加对右边非0元素索引的记录，避免每次都从当前0元素的位置开始向后查找
    """
    new_idx = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            if new_idx == -1:
                new_idx = i
            while new_idx < len(nums):
                if nums[new_idx] != 0:
                    nums[i] = nums[new_idx]
                    nums[new_idx] = 0
                    break
                new_idx += 1
    return nums


if __name__ == "__main__":
    tst_arr = [0, 1, 0, 3, 12]
    print(solve1(tst_arr))
    ...
