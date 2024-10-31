"""
xxx
"""


def solve(s):
    len_s = len(s)

    res = []
    for i in range(len_s):
        sgl_arr = [0] * len_s
        sgl_arr[i] = 1
        res.append(sgl_arr)

    for i in range(len_s - 1, -1, -1):
        for j in range(i + 1, len_s):  # 从i+1开始，避免对对角线上的元素重复操作
            if s[i] == s[j]:
                res[i][j] = res[i + 1][j - 1] + 2
            else:
                res[i][j] = max(res[i][j - 1], res[i + 1][j - 1], res[i + 1][j])

    return max([max(e) for e in res])


if __name__ == "__main__":
    print(solve("bbbab"))
    print(solve("cbbd"))
    print(solve(
        "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"))
    ...
