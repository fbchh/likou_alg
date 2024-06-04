"""
xxx
"""
from time import time


def tol_time(func):
    def inner_func(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f"[info] tol cost sec: {t2 - t1}")
        return res

    return inner_func


def solve1(nums, s):
    """
    暴力法
    :param nums:
    :param s:
    :return:
    """
    res = []
    i = 0
    while i < len(nums):
        j = i
        while j < len(nums):
            sgl_nums = nums[i:j + 1]
            if sum(sgl_nums) >= s:
                if len(res) == 0:
                    res = sgl_nums
                else:
                    if len(res) > len(sgl_nums):
                        res = sgl_nums
                break
            else:
                j += 1

        i += 1
    return len(res)


def solve2(nums, s):
    """
    暴力法的优化——使用一个循环，注意使用优化后的方法就不要再使用sum方法了，这种方式每次都计算了大量的重复元素
    :param nums:
    :param s:
    :return:
    """
    r = 0
    l = 0
    res = []
    cur_sum = 0
    while r < len(nums):
        cur_sum += nums[r]
        if cur_sum >= s:
            while cur_sum >= s:
                if r - l + 1 < len(res) or len(res) == 0:
                    res = nums[l: r + 1]
                cur_sum -= nums[l]
                l += 1
        r += 1
    return len(res)


if __name__ == "__main__":
    tst1 = [2, 3, 1, 2, 4, 3]
    tst2 = [1, 4, 4]
    tst3 = [1, 1, 1, 1, 1, 1, 1, 1]
    tst4 = [1, 2, 3, 4, 5]

    # print(solve1(tst1, 7))
    # print(solve1(tst2, 4))
    # print(solve1(tst3, 11))

    print(solve2(tst1, 7))
    print(solve2(tst2, 4))
    print(solve2(tst3, 11))
    print(solve2(tst4, 11))
    pass
