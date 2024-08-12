"""
xxx
"""


def solve(nums):
    _len = len(nums)
    if _len == 1:
        return 0

    res = 0
    last_cover = 0
    cur_cover = 0
    for i in range(_len):
        cur_cover = max(cur_cover, i + nums[i])
        if i == last_cover:
            res += 1
            last_cover = cur_cover
            if last_cover >= _len - 1:
                return res


if __name__ == "__main__":
    print(solve([2, 3, 1, 1, 4]))
    print(solve([2, 3, 0, 1, 4]))
    ...
