"""
xxx
"""


def solve(prices):
    # 动规
    len_prices = len(prices)
    res = [[0, 0]] * len_prices  # [持有最大，不持有最大]

    res[0] = [-prices[0], 0]
    for i in range(1, len_prices):
        res[i][0] = max(-prices[i], res[i - 1][0])
        res[i][1] = max(prices[i] + res[i - 1][0], res[i - 1][1])

    return res[-1][-1]


def solve1(prices):
    # 贪心
    l = pow(10, 4)
    res = 0

    for e in prices:
        l = min(e, l)
        res = max(e - l, res)

    return res


if __name__ == "__main__":
    print(solve([7, 1, 5, 3, 6, 4]))
    print(solve1([7, 1, 5, 3, 6, 4]))
    ...
