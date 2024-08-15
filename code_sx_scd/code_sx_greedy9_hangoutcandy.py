"""
xxx
"""


def solve(ratings):
    res1 = [1]
    res2 = [1]  # 记得reverse

    _len = len(ratings)
    idx = 1
    while idx < _len:
        _ = res1[-1] + 1 if ratings[idx] > ratings[idx - 1] else 1
        res1.append(_)
        idx += 1

    idx = _len - 2
    while idx > -1:
        _ = res2[-1] + 1 if ratings[idx] > ratings[idx + 1] else 1
        res2.append(_)
        idx -= 1
    res2.reverse()

    return sum([max(res1[i], res2[i]) for i in range(_len)])


if __name__ == "__main__":
    print(solve([1, 0, 2]))
    print(solve([1, 2, 2]))
    ...
