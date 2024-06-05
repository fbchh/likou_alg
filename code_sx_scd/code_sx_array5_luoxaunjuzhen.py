"""
xxx
"""


def solve1(n):
    if n < 0:
        return []

    res = [[0 for _1 in range(n)] for _ in range(n)]
    val = 1

    index = 0
    while n > 2 * index:
        # up row
        i, j = index, index
        while j < n - index:
            res[i][j] = val
            j += 1
            val += 1

        # r column
        i += 1
        j -= 1
        while i < n - index:
            res[i][j] = val
            i += 1
            val += 1

        # down row
        j -= 1
        i -= 1
        while j >= index:
            res[i][j] = val
            j -= 1
            val += 1

        # l column
        i -= 1
        j += 1
        while i > index:
            res[i][j] = val
            i -= 1
            val += 1

        index += 1
    return res


if __name__ == "__main__":
    tst1 = 2
    tst2 = 3
    tst3 = 4
    tst4 = 5
    tst5 = 100

    print(solve1(tst1))
    print(solve1(tst2))
    print(solve1(tst3))
    print(solve1(tst4))
    print(solve1(tst5))
    pass
