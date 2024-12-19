"""
xxx
"""


def solve(nums, k):
    def inner_func(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    _len = len(nums)
    k %= _len
    inner_func(0, _len - 1)
    inner_func(0, k - 1)
    inner_func(k, _len - 1)
    return nums


if __name__ == "__main__":
    tst_arr1 = [1, 2, 3, 4, 5, 6, 7]
    tst_arr2 = [-1, -100, 3, 99]

    print(solve(tst_arr1, 3))
    print(solve(tst_arr2, 2))
    ...
