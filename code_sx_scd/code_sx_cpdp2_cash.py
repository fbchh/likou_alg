"""
xxx
"""


def solve(amount, coins):
    res = [0] * (amount + 1)
    res[0] = 1

    for coin in coins:
        for j in range(coin, amount + 1):
            res[j] = res[j] + 1 * res[j - coin]

    return res[-1]


if __name__ == "__main__":
    print(solve(5, [1, 2, 5]))
    print(solve(3, [2]))
    print(solve(10, [10]))
    print(solve(0, [7]))
    ...
