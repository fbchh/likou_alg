"""
xxx
"""


def solve1(nums: list, target: int):
    """
    在数组(无重复元素、升序)中二分查找指定值，不存在返回-1，存在返回其索引
    :param nums: xx
    :param target: xx
    :return: idx
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1
        else:
            return m
    return -1


if __name__ == "__main__":
    pass
