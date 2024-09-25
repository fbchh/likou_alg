"""
xxx
"""


def solve(n):
    inner_max = pow(10, 10)
    res = [inner_max] * (n + 1)
    res[0] = 0
    nums = [pow(e, 2) for e in range(1, n + 1) if pow(e, 2) <= n]

    for e in nums:
        for j in range(e, n + 1):
            res[j] = min(res[j], 1 + res[j - e])

    return res[-1]


if __name__ == "__main__":
    print(solve(5))
    print(solve(12))
    print(solve(13))
    ...
