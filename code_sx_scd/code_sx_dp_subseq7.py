"""
xxx
"""


def solve(s, t):
    len_t = len(t)
    res = [-1] * (len_t + 1)

    for i in range(1, len_t + 1):
        if res[i - 1] + 1 < len(s) and t[i - 1] == s[res[i - 1] + 1]:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i - 1]

    return len(s) == res[-1] + 1


def solve1(s, t):
    # 随想录官方解法
    len_s = len(s)
    len_t = len(t)

    res = []
    for i in range(len_s + 1):
        res.append([0] * (len_t + 1))

    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = res[i][j - 1]

    return res[-1][-1] == len(s)


if __name__ == "__main__":
    # print(solve("abc", "ahbgdc"))
    # print(solve("axc", "ahbgdc"))
    # print(solve("", "ahbgdc"))

    print(solve1("abc", "ahbgdc"))
    print(solve1("axc", "ahbgdc"))
    print(solve1("", "ahbgdc"))
    ...
