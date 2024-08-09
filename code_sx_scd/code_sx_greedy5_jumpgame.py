"""
xxx
"""


def solve(nums):
    """
    手撸版本（有问题，未优化）
    思路是一致的，实现方法和随想录官方给出的还是存在差异
    """
    _len = len(nums)
    if _len == 0:
        return True

    idx = 0
    while idx < _len - 1:
        cur_cover = nums[idx] + idx

        if cur_cover >= _len - 1:
            return True

        if idx == cur_cover:
            return False

        next_idx = cur_cover
        for j in range(idx + 1, cur_cover):
            _ = j + nums[j]
            if _ > cur_cover:
                next_idx = _

        idx = next_idx
    return True


def solve1(nums):
    _len = len(nums)
    if _len == 1:
        return True

    cover = 0
    for i in range(_len):
        if i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= _len - 1:
                return True

    return False


if __name__ == "__main__":
    tst_nums = [3, 2, 1, 0, 4]
    # print(solve(tst_nums))
    # print(solve([2, 3, 1, 1, 4]))
    # print(solve([1, 3, 2]))
    # print(solve([0]))
    # print(solve([2, 0, 0]))
    # print(solve([2, 5, 0, 0]))
    # print(solve([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))  # real: True my_ans:False

    print(solve1(tst_nums))
    print(solve1([2, 3, 1, 1, 4]))
    print(solve1([1, 3, 2]))
    print(solve1([0]))
    print(solve1([2, 0, 0]))
    print(solve1([2, 5, 0, 0]))
    print(solve1([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))  # real: True my_ans:False
    ...
