"""
xxx
"""


def solve(nums):
    len_nums = len(nums)
    max_nums = max(nums)

    spec_num = -0.1
    res = [spec_num] * len_nums

    idx = 1
    _stack = [0]
    while len(_stack) > 0:
        if idx == len_nums:
            idx = 0
        else:
            for i in range(idx, len_nums):
                if nums[i] > nums[_stack[-1]]:
                    while len(_stack) > 0 and nums[_stack[-1]] < nums[i]:
                        res[_stack[-1]] = nums[i]
                        _stack.pop()
                if res[i] == spec_num:
                    _stack.append(i)
                idx += 1
            while len(_stack) > 0 and nums[_stack[-1]] == max_nums:
                _stack.pop()
    return [-1 if e == spec_num else e for e in res]


def solve1(nums):
    len_nums = len(nums)
    res = [-1] * len_nums

    _stack = [0]
    for i in range(1, len_nums * 2):
        if nums[i % len_nums] > nums[_stack[-1] % len_nums]:
            res[_stack[-1]] = nums[i % len_nums]
            _stack.pop()

        _stack.append(i % len_nums)

    return res


if __name__ == "__main__":
    # print(solve([1, 2, 1]))
    # print(solve([1, 2, 3, 4, 3]))
    # print(solve([-1, -2]))

    print(solve1([1, 2, 1]))
    print(solve1([1, 2, 3, 4, 3]))
    print(solve1([-1, -2]))
    ...
