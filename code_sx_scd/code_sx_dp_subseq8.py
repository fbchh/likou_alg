"""
xxx
"""


def solve(s, t):
    len_s = len(s)
    len_t = len(t)
    res = []
    for i in range(len_s + 1):
        sub_row = [0] * (len_t + 1)
        sub_row[0] = 1
        res.append(sub_row)

    for i in range(1, len_s + 1):
        for j in range(1, len_t + 1):
            if s[i - 1] == t[j - 1]:
                res[i][j] = res[i - 1][j] + res[i - 1][j - 1]
            else:
                res[i][j] = res[i - 1][j]

    return res[-1][-1]


if __name__ == "__main__":
    print(solve("rabbbit", "rabbit"))
    print(solve("babgbag", "bag"))
    ...
