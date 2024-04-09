"""
代码随想录学习记录
章节：栈与队列
题目：前K个高频元素

    题意：
    给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

    示例 1:
        输入: nums = [1,1,1,2,2,3], k = 2
        输出: [1,2]

    示例 2:
        输入: nums = [1], k = 1
        输出: [1]

    提示：
        你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
        你的算法的时间复杂度必须优于 $O(n \log n)$ , n 是数组的大小。
        题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
        你可以按任意顺序返回答案。
"""


def solve1(nums, k):
    """
    解法1，基于dict的计数器
    :param k: xx
    :param nums: xx
    :return: xx
    """
    _record = dict()
    for e in nums:
        _record[e] = _record.get(e, 0) + 1

    _record = list(_record.items())
    _record = sorted(_record, key=lambda e1: e1[1], reverse=True)

    return [e[0] for e in _record[0:k]]


def solve2(nums, k):
    """
    解法2，利用语言本身的“堆”的数据结构，往该数据结构中push元素的时候会自动排序，语言内部的“堆”数据结构底层有二叉树这种数据结构，一刷暂时不考虑实现
    :param nums: xx
    :param k: xx
    :return: xx
    """
    pass


if __name__ == "__main__":
    print(solve1([1, 1, 1, 2, 2, 3], 2))
    print(solve1([4, 1, -1, 2, -1, 2, 3], 2))
    pass
