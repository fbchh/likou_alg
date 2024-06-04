"""
xxx
"""
from time import time


def tol_time(func):
    """
    统计耗时
    :param func:
    :return:
    """

    def inner_func(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f"[info] tol cost sec: {t2 - t1}")
        return res

    return inner_func


@tol_time
def solve1(nums):
    """
    api战士
    :param nums:
    :return:
    """
    nums = [pow(e, 2) for e in nums]
    nums.sort()
    return nums


@tol_time
def solve2(nums):
    """
    双指针+新数组
    :param nums:
    :return:
    """
    nums1 = [0] * len(nums)
    k = len(nums1) - 1
    l, r = 0, len(nums) - 1
    while l <= r:
        l_res = pow(nums[l], 2)
        r_res = pow(nums[r], 2)
        if l_res <= r_res:
            nums1[k] = r_res
            r -= 1
        else:
            nums1[k] = l_res
            l += 1

        k -= 1
    return nums1


if __name__ == "__main__":
    tst1 = [-4, -1, 0, 3, 10]
    tst2 = [-7, -3, 2, 3, 11]

    print(solve1(tst1))
    print(solve1(tst2))

    print(solve2(tst1))
    print(solve2(tst2))
    pass
