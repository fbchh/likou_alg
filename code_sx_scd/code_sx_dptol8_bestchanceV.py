"""
xxx
"""


def solve(prices):
    res = [0, 0, 0, 0]
    res[0] = -prices[0]  # 持有 （昨天持有、昨天冷却今天买入、昨天保持不持有今天买入）
    res[1] = 0  # 保持不持有 （昨天冷却、昨天保持不持有）
    res[2] = 0  # 今天卖出 (昨天持有)
    res[3] = 0  # 冷却 （昨天卖出）

    for i in range(1, len(prices)):
        l_res = [e for e in res]
        res[0] = max(l_res[0], l_res[3] - prices[i], l_res[1] - prices[i])
        res[1] = max(l_res[3], l_res[1])
        res[2] = l_res[0] + prices[i]
        res[3] = l_res[2]

    return max(res[2], res[1])


if __name__ == "__main__":
    print(solve([1, 2, 3, 0, 2]))
    print(solve([2, 1]))
    ...
