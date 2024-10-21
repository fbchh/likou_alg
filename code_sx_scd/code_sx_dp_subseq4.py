"""
xxx
"""


def solve(text1, text2):
    len_nums1 = len(text1)
    len_nums2 = len(text2)

    res = []
    for i in range(len_nums2 + 1):
        res.append([0] * (len_nums1 + 1))

    for i in range(1, len_nums2 + 1):
        for j in range(1, len_nums1 + 1):
            if text2[i - 1] == text1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return max([max(e) for e in res])


if __name__ == "__main__":
    print(solve("abcde", "ace"))
    print(solve("abc", "abc"))
    print(solve("abc", "def"))
    ...
