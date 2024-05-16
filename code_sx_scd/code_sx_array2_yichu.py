"""
xxx
"""


def solve1(nums: list, val: int):
    """
    原地移除数组中指定数值的元素
    :param nums: xx
    :param val: xx
    :return: xx
    """
    low_idx = 0
    for fast_idx in range(len(nums)):
        if nums[fast_idx] != val:
            nums[low_idx] = nums[fast_idx]
            low_idx += 1

    return low_idx


if __name__ == "__main__":
    pass
