"""
xxx
"""
from time import time


def cal_time(func):
    def inner_func(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        print(f"tol cost sec: {t2 - t1}")
        return res

    return inner_func


@cal_time
def solve1(nums):  # 卡在力扣的最后几个测试用例上，超出时间限制 经过本地验证是正确的
    _nums = sorted(nums)

    _tol = []
    _last_num1 = None
    for i in range(len(_nums)):
        if _nums[i] == _last_num1 and len(_tol) > 0 and _tol[-1][0] == _nums[i]:
            continue
        if i + 1 < len(_nums):
            _nums1 = _nums[i + 1:]
            _last_num2 = None
            for j in range(len(_nums1)):
                if _nums1[j] == _last_num2 and len(_tol) > 0 and _tol[-1][1] == _nums1[j]:
                    continue
                if j + 1 < len(_nums1):
                    _sum = _nums[i] + _nums1[j]
                    _nums2 = _nums1[j + 1:]
                    if _nums2[0] > -_sum or _nums2[-1] < -_sum:
                        continue
                    if -_sum in _nums2:
                        _tol.append([_nums[i], _nums1[j], -_sum])
                        _last_num1 = _nums[i]
                        _last_num2 = _nums1[j]
    return _tol


@cal_time
def solve2(nums):  # 相比于第一种方法，在处理力扣的最后几个大数组非常快，第308组测试数据上面方法约为16秒，这个方法用时0.26秒，再次证实指针思想的优越性
    _nums = sorted(nums)
    if _nums[-1] < 0:
        return []

    res = []
    _len = len(_nums)
    for i in range(len(_nums)):
        if _nums[i] > 0:
            break
        if i > 0 and _nums[i] == _nums[i - 1]:
            continue

        p2 = _len - 1
        p1 = i + 1
        while p1 < p2:
            _sum = _nums[i] + _nums[p1] + _nums[p2]
            if _sum < 0:
                p1 += 1
            elif _sum > 0:
                p2 -= 1
            else:
                res.append([_nums[i], _nums[p1], _nums[p2]])
                while p2 > p1 and _nums[p2] == _nums[p2 - 1]:
                    p2 -= 1
                while p2 > p1 and _nums[p1] == _nums[p1 + 1]:
                    p1 += 1
                p2 -= 1
                p1 += 1
    return res


if __name__ == "__main__":
    tst_ege1 = [-1, 0, 1, 2, -1, -4]
    print(solve1(tst_ege1))
    print(solve1([0, 0, 0, 0]))
    print(solve1([1, -1, -1, 0]))
    print(solve1([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))

    print(solve2(tst_ege1))
    print(solve2([0, 0, 0, 0]))
    print(solve2([1, -1, -1, 0]))
    print(solve2([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
    pass
