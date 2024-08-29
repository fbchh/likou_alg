"""
xxx
"""


def solve(n):
    res = [1, 2]
    if n <= 2:
        return res[n - 1]

    for i in range(n - 2):
        _ = res[1]
        res[1] = sum(res)
        res[0] = _

    return res[1]


if __name__ == "__main__":
    print(solve(3))
    print(solve(4))
    ...
