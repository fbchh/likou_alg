"""
xxx
"""


def solve(prices):
    # 模拟的思路 取上升或者平稳阶段的价格差即可
    res = 0
    l = prices[0]

    for i in range(1, len(prices)):
        cur_res = prices[i] - l
        if cur_res >= 0:
            res += cur_res
        l = prices[i]

    return res


def solve1(prices):
    len_arr = len(prices)
    res = [[0, 0]] * len_arr  # 持有，不持有
    res[0][0] = -prices[0]
    res[0][1] = 0

    for i in range(1, len_arr):
        res[i][0] = max(res[i - 1][0], res[i - 1][1] - prices[i])
        res[i][1] = max(res[i - 1][0] + prices[i], res[i - 1][1])

    return res[-1][-1]


if __name__ == "__main__":
    print(solve([7, 1, 5, 3, 6, 4]))
    print(solve1([7, 1, 5, 3, 6, 4]))
    ...
