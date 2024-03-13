"""
代码随想录学习记录
章节：数组
题目：长度最小的子数组

    给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

    示例：
    输入：s = 7, nums = [2,3,1,2,4,3]
    输出：2
    解释：子数组 [4,3] 是该条件下的长度最小的子数组。

    提示：
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
"""


def solve1(input_nums, input_s):
    """
    解法1，顺序遍历，自称为左右指针法，代码随想录里叫做滑动窗口
    :param input_s:xx
    :param input_nums:xx
    :return:xx
    """
    _c_num = 0
    _last_len = len(input_nums)
    l = 0
    for i in range(len(input_nums)):
        _c_num += input_nums[i]
        if _c_num >= input_s:
            _len = i + 1 - l
            _last_len = _last_len if _last_len <= _len else _len
            l = i + 1
            _c_num = 0  # 初始化“新区间和”
    _last_len = 0 if _last_len == len(input_nums) else _last_len
    return _last_len


if __name__ == "__main__":
    from time import time

    t1 = time()

    print(solve1([2, 3, 1, 2, 4, 3], 7))
    print(solve1([1, 4, 4], 4))
    print(solve1([1, 1, 1, 1, 1, 1, 1, 1], 11))

    t2 = time()
    print(f"[info] tol cost sec: {t2 - t1}S")
