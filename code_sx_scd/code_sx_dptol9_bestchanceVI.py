"""
xxx
"""


def solve(prices, fee):
    res = [-prices[0], 0, -fee]

    for i in range(len(prices)):
        last_day = [e for e in res]
        res[0] = max(last_day[0], last_day[2] - prices[i], last_day[1] - prices[i])  # 持有（昨天持有、昨天卖出、昨天保持不持有）
        res[1] = max(last_day[1], last_day[2])  # 保持不持有（昨天保持不持有、昨天卖出）
        res[2] = last_day[0] + prices[i] - fee  # 今卖出（昨天持有）

    return max(res[1], res[2])


if __name__ == "__main__":
    print(solve([1, 3, 2, 8, 4, 9], 2))
    print(solve([1, 3, 7, 5, 10, 3], 3))
    ...
