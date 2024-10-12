"""
xxx
"""


def solve(prices):
    len_arr = len(prices)
    res = [[0, 0, 0, 0, 0]] * len_arr

    res[0] = [0, -prices[0], 0, -prices[0], 0]  # 没有操作；第一次持有；第一次不持有；第二次持有；第二次不持有

    for i in range(1, len_arr):
        res[i][1] = max(res[i - 1][1], res[i - 1][0] - prices[i])
        res[i][2] = max(res[i - 1][1] + prices[i], res[i - 1][2])
        res[i][3] = max(res[i - 1][3], res[i - 1][2] - prices[i])
        res[i][4] = max(res[i - 1][3] + prices[i], res[i - 1][4])

    return res[-1][-1]


if __name__ == "__main__":
    print(solve([1, 2, 3, 4, 5, 2, 3, 4, 5, 6]))
    print(solve([3, 3, 5, 0, 0, 3, 1, 4]))
    ...
