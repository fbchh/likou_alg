"""
xxx
"""


def solve(coins, amount):
    inner_max = pow(10, 10)
    res = [inner_max] * (amount + 1)
    res[0] = 0

    for e in coins:
        for j in range(e, amount + 1):
            res[j] = min(res[j], 1 + res[j - e])

    return -1 if res[-1] == inner_max else res[-1]


if __name__ == "__main__":
    print(solve([1, 2, 5], 11))
    print(solve([2], 3))
    print(solve([1], 0))
    ...
