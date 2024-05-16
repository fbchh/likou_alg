"""
代码随想录学习记录
章节：栈和队列
题目：滑动窗口最大值

    题意：
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
    返回滑动窗口中的最大值。
"""


def solve1(nums, k):
    """
    解法1，数组切片 + 排序api
    :param nums: xx
    :param k: xx
    :return: xx
    """
    _res = []
    for i in range(len(nums)):
        _window_arr = nums[i:i + k]
        if len(_window_arr) == k:
            _res.append(max(_window_arr))
    return _res


def solve2(nums, k):
    """
    解法2，基于单调队列，每次窗口移动涉及到的操作就是push和pop，详情参考随香炉官方说明
    :param nums: xx
    :param k: xx
    :return: xx
    """
    pass


if __name__ == "__main__":
    print(solve1([1, 3, -1, -3, 5, 3, 6, 7], 3))
    pass
