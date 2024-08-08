"""
xxx
"""


def solve(prices):
    _len = len(prices)
    if _len == 1:
        return 0

    res = []
    count = 0
    for i in range(_len):
        if i < _len - 1:
            cur_diff = prices[i + 1] - prices[i]
            if count != 0 and cur_diff < 0:
                res.append(count)
                count = 0

            if cur_diff > 0:
                count += cur_diff
        else:
            if count != 0:
                res.append(count)
    return sum(res)


if __name__ == "__main__":
    tst_proces = [7, 1, 5, 3, 6, 4]
    print(solve(tst_proces))
    print(solve([1, 2, 3, 4, 5]))
    print(solve([7, 6, 4, 3, 1]))
    ...
