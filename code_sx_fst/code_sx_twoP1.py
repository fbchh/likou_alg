"""
代码随想录学习记录
章节：双指针法
题目：移除元素

    题意：
    给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
    不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
    元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

    示例 1: 给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 你不需要考虑数组中超出新长度后面的元素。
    示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

    你不需要考虑数组中超出新长度后面的元素
"""


def solve1(nums, val):
    """
    解法1，暴力法
    :param nums: xx
    :param val: xx
    :return: xx
    """
    for i in range(len(nums)):
        if nums[i] == val:
            r = i
            while nums[r] == val:
                if r == len(nums) - 1:
                    return i
                r += 1
            nums[r], nums[i] = nums[i], nums[r]


def solve2(nums, val):
    """
    双指针法之快慢指针，将“非”元素放到左边，遍历一遍，返回慢指针即可
    :param nums: xx
    :param val: xx
    :return: xx
    """
    l = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l] = nums[i]
            l += 1
    return l


if __name__ == "__main__":
    print(solve1([3, 2, 2, 3], 3))
    print(solve1([0, 1, 2, 2, 3, 0, 4, 2], 2))

    print(solve2([3, 2, 2, 3], 3))
    print(solve2([0, 1, 2, 2, 3, 0, 4, 2], 2))
    pass
