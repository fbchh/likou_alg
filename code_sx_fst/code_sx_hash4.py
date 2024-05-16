"""
代码随想录学习记录
章节：哈希表
题目：两数之和

    题意：

    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
"""


def solve1(input_nums, num):
    """
    解法1，嵌套循环，逐个排除
    :param input_nums:xx
    :param num:xx
    :return:xx
    """
    for i in range(len(input_nums)):
        _num1 = num - input_nums[i]
        _nums = input_nums[i + 1:]
        if _num1 in _nums:
            return [_nums.index(_num1) + i + 1, i]


def solve2(input_nums, num):
    """
    解法2，基于dict，实现val-index的数据结构，遍历元素，然后判断
    :param input_nums: xx
    :param num: xx
    :return: xx
    """
    _nums = {}
    for i, e in enumerate(input_nums):
        if num - e in _nums:
            return [i, _nums[num - e]]
        _nums[e] = i


if __name__ == "__main__":
    print(solve1([2, 7, 11, 15], 9))

    print(solve1([3, 2, 4], 6))

    print(solve2([3, 2, 4], 6))
    print(solve2([2, 7, 11, 15], 9))
