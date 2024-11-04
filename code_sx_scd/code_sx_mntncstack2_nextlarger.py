"""
xxx
"""


def solve(nums1, nums2):
    nums1.reverse()
    len_nums2 = len(nums2)

    res = []
    while len(nums1) > 0:
        inner_len = len(nums1)

        inner_idx = nums2.index(nums1[-1])
        if -1 < inner_idx < len_nums2 - 1:
            for i in range(inner_idx + 1, len_nums2):
                if nums2[i] > nums1[-1]:
                    nums1.pop()
                    res.append(nums2[i])
                    break

        if len(nums1) == inner_len:
            res.append(-1)
            nums1.pop()

    return res


def solve1(nums1, nums2):
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)

    res = [-1] * len_nums1

    _stack = [0]  # nums2 ele idx
    for i in range(1, len_nums2):
        if nums2[i] > nums2[_stack[-1]]:
            while len(_stack) > 0 and nums2[i] > nums2[_stack[-1]]:
                if nums2[_stack[-1]] in nums1:
                    inner_idx = nums1.index(nums2[_stack[-1]])
                    res[inner_idx] = nums2[i]
                _stack.pop()
        _stack.append(i)

    return res


if __name__ == "__main__":
    # print(solve([4, 1, 2], [1, 3, 4, 2]))
    # print(solve([2, 4], [1, 2, 3, 4]))

    print(solve1([4, 1, 2], [1, 3, 4, 2]))
    print(solve1([2, 4], [1, 2, 3, 4]))
    ...
