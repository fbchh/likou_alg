"""
xxx
理解题意其实就是求最长公共子序列
"""


def solve(nums1, nums2):
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)

    # init
    res = []
    for i in range(len_nums2 + 1):
        res.append([0] * (len_nums1 + 1))

    for i in range(1, len_nums2 + 1):
        for j in range(1, len_nums1 + 1):
            if nums2[i - 1] == nums1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = max(res[i][j - 1], res[i - 1][j])

    return max(max(res))


if __name__ == "__main__":
    print(solve([1, 4, 2], [1, 2, 4]))
    ...
