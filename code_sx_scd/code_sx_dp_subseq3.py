"""
xxx
"""


def solve(nums1, nums2):
    len_num1 = len(nums1)
    len_nums2 = len(nums2)

    res = []
    for _ in range(len_nums2 + 1):
        res.append([0] * (len_num1 + 1))

    for i in range(1, len_nums2 + 1):
        for j in range(1, len_num1 + 1):
            if nums2[i - 1] == nums1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
    return max([max(e) for e in res])


if __name__ == "__main__":
    print(solve([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(solve([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
    print(solve([1, 0, 0, 0, 1], [1, 0, 0, 1, 0]))
    print(solve([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]))
    print(solve([1, 1, 0, 0, 1, 1], [0, 0]))
    ...
