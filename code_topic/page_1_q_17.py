"""
 @Time: 2025/4/28 9:29
 @Auther: FBC
"""


def solve(prices):
    # 暴力
    prices_len = len(prices)

    cur_profit = 0
    for i in range(prices_len):
        for j in range(i + 1, prices_len):
            sgl_profit = prices[j] - prices[i]
            if sgl_profit > 0:
                cur_profit = max(cur_profit, sgl_profit)
    return cur_profit


def solve1(prices):
    # 贪心
    min_in = prices[0]
    max_profit = 0

    for e in prices:
        min_in = min(min_in, e)
        max_profit = max(max_profit, e - min_in)

    return max_profit


def solve2(prices):
    # 动规
    # 持有（保持持有/买入）
    # 不持有（保持不持有/卖出）

    prices_len = len(prices)
    res = [[0, 0]] * prices_len

    res[0] = [-prices[0], 0]
    for i in range(1, prices_len):
        res[i][0] = max(res[i - 1][0], -prices[i])  # 持有
        res[i][1] = max(res[i - 1][1], res[i - 1][0] + prices[i])  # 不持有
    return res[-1][1]


if __name__ == "__main__":
    tst_prices1 = [7, 1, 5, 3, 6, 4]  # 5
    tst_prices2 = [7, 6, 4, 3, 1]  # 0

    print(solve(tst_prices1))
    print(solve(tst_prices2))

    print(solve1(tst_prices1))
    print(solve1(tst_prices2))

    print(solve2(tst_prices1))
    print(solve2(tst_prices2))
    ...
