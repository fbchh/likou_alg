"""
xxx
"""


def solve(s):
    len_s = len(s)
    res = []
    for i in range(len_s):
        res.append([0] * len_s)

    # 左下至右上
    for i in range(len_s - 1, -1, -1):
        for j in range(i, len_s):
            if s[i] == s[j] and (j - i in [0, 1] or res[i + 1][j - 1] == 1):
                res[i][j] = 1

    return sum([sum(e) for e in res])


if __name__ == "__main__":
    print(solve("abc"))
    print(solve("aaa"))
    ...
