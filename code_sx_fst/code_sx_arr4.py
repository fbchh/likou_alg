"""
代码随想录学习记录
章节：数组
题目：有序数组的平方

    给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

    示例 1：
    输入：nums = [-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]

    示例 2：
    输入：nums = [-7,-3,2,3,11]
    输出：[4,9,9,49,121]
"""


def slove1(input_nums):
    """
    解法1，使用py内置排序方法
    :param input_nums:xx
    :return: xx
    """
    input_nums = [pow(e, 2) for e in input_nums]
    input_nums.sort()
    return input_nums


def slove2(input_nums):
    """
    解法2，新数组+左右指针
    :param input_nums:xx
    :return:xx
    """
    l = 0
    r = len(input_nums) - 1
    _res = list(range(len(input_nums)))
    i = len(input_nums) - 1
    while l <= r:
        l_num = pow(input_nums[l], 2)
        r_num = pow(input_nums[r], 2)

        if l_num < r_num:
            _res[i] = r_num
            r -= 1
        elif l_num >= r_num:
            _res[i] = l_num
            l += 1
        i -= 1

    return _res


if __name__ == "__main__":
    from time import time

    t1 = time()

    tst_nums1 = [-4, -1, 0, 3, 10]
    tst_nums2 = [-7, -3, 2, 3, 11]

    print(slove1(tst_nums1))
    print(slove1(tst_nums2))

    t2 = time()
    print(f"[info] tol cost sec: {t2 - t1}S")

    print(slove2(tst_nums1))
    print(slove2(tst_nums2))

    t3 = time()
    print(f"[info] tol cost sec: {t3 - t2}S")
