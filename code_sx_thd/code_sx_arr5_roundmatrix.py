"""
xxx
"""


def solve(n):
    if n == 1:
        return [[0]]

    iter_num = n // 2
    mid_num = n % 2
    res = [[0] * n for _ in range(n)]
    count = 1

    for i in range(iter_num):
        # up
        for l1 in range(i, n - i):
            res[i][l1] = count
            count += 1

        # right
        for r2 in range(i + 1, n - i):
            res[r2][n - 1 - i] = count
            count += 1

        # down
        for l2 in range(n - i - 2, -1 + i, -1):
            res[n - 1 - i][l2] = count
            count += 1

        # left
        for c2 in range(n - 2 - i, 0 + i, -1):
            res[c2][i] = count
            count += 1

        # 奇
        if mid_num != 0:
            res[iter_num][iter_num] = count

    return res


def tst():
    print(solve(3))
    print(solve(4))
    print(solve(5))


if __name__ == "__main__":
    tst()
    ...
