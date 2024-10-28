"""
xxx
"""


def solve(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)
    res = []
    for i in range(len_word1 + 1):
        sgl_arr = [j for j in range(len_word2 + 1)]
        sgl_arr[0] = i
        res.append(sgl_arr)

    for i in range(1, len_word1 + 1):
        for j in range(1, len_word2 + 1):
            if word1[i - 1] == word2[j - 1]:
                res[i][j] = res[i - 1][j - 1]
            else:
                res[i][j] = min(res[i - 1][j] + 1, res[i][j - 1] + 1, res[i - 1][j - 1] + 2)

    return res[-1][-1]


if __name__ == '__main__':
    print(solve("sea", "eat"))
    print(solve("leetcode", "etco"))
    ...
