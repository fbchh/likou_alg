"""
xxx
"""


def solve(n, m):
    res = [0] * (n + 1)
    res[0] = 1
    vals = [i for i in range(1, m + 1)]

    for i in range(n + 1):
        for e in vals:
            if i >= e:
                res[i] += res[i - e]
    return res[-1]


if __name__ == "__main__":
    print(solve(3, 2))
    ...
