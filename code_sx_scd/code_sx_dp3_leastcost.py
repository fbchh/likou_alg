"""
xxx
"""


def solve(cost):
    ll_num = 0
    l_num = 0

    if len(cost) > 2:
        for i in range(2, len(cost) + 1):
            _ = l_num
            l_num = min(cost[i - 1] + l_num, cost[i - 2] + ll_num)
            ll_num = _

    return l_num


if __name__ == "__main__":
    print(solve([10, 15, 20]))
    print(solve([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    ...
