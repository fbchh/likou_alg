"""
xxx
"""


def solve(word1, word2):
    len_world1 = len(word1)
    len_world2 = len(word2)

    res = []
    for i in range(len_world1 + 1):
        if i == 0:
            sgl_arr = [i1 for i1 in range(len_world2 + 1)]
        else:
            sgl_arr = [0] * (len_world2 + 1)
        sgl_arr[0] = i
        res.append(sgl_arr)

    for i in range(1, len_world1 + 1):
        for j in range(1, len_world2 + 1):
            if word1[i - 1] == word2[j - 1]:
                res[i][j] = res[i - 1][j - 1]
            else:
                res[i][j] = min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1]) + 1  # 替换、插入、删除

    return res[-1][-1]


if __name__ == "__main__":
    print(solve("horse", "ros"))
    print(solve("intention", "execution"))
    ...
