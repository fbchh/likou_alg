"""
代码随想录学习记录
章节：哈希表
题目：两个数组的交集

    题意：

    给定两个数组，编写一个函数来计算它们的交集。
    示例1：
    输入： nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    输出： [2]

    示例2：
    输入： nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    输出： [9, 4]

    说明：
    输出结果中的每个元素一定是唯一的。 我们可以不考虑输出结果的顺序
"""
from time import time


def count_time(input_fun):
    t1 = time()
    input_fun()
    print(f"[info] tol cost sec: {time() - t1}S")


def solve1(input_nums1, input_nums2):
    """
    解法1，先将输入的两个数组去重，遍历长度较短的数组，判断其元素是否在另外一个数组中，存在则作为结果之一，然后输出
    :param input_nums1: xx
    :param input_nums2: xx
    :return: xx
    """

    _nums1 = list(set(input_nums1))
    _nums2 = list(set(input_nums2))

    _ing, _tar = (_nums2, _nums1) if len(_nums1) >= len(_nums2) else (_nums1, _nums2)
    _res = []
    for e in _ing:
        if e in _tar:
            _res.append(e)

    return _res


def solve2(input_nums1, input_nums2):
    """
    解法2，如果输入的两个数组的长度和内部元素的值有区间限制，则可以使用hash法(这里假定的条件是输入的两个数组中的元素范围：[0,1000])
    :param input_nums1: xx
    :param input_nums2: xx
    :return: xx
    """
    _hash_list = [0] * 1001
    input_nums1 = list(set(input_nums1))
    input_nums2 = list(set(input_nums2))
    _res = []
    for e in input_nums1:
        _hash_list[e] = 1
    for e in input_nums2:
        if _hash_list[e] == 1:
            _res.append(e)
    return _res


def solve3(input_nums1, input_nums2):
    """
    艺术法！！！,要求对语言的原生数据结构熟悉
    :param input_nums1:xxx
    :param input_nums2:xxx
    :return:xxx
    """
    return list(set(input_nums1) & set(input_nums2))


if __name__ == "__main__":
    def tst1():
        print(solve1(list(range(1000)), [1, 3, 3, 3, 7, 10, 999]))
    count_time(tst1)

    def tst2():
        print(solve2(list(range(1000)), [1, 3, 3, 3, 7, 10, 999]))
    count_time(tst2)

    def tst3():
        print(solve3(list(range(1000)), [1, 3, 3, 3, 7, 10, 999]))
    count_time(tst3)
