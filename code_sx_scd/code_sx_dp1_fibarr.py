"""
xxx
"""


def solve(n):
    if n == 0:
        return 0
    l = 0
    r = 1

    for i in range(n - 1):
        hist_r = r
        r = l + r
        l = hist_r

    return r


if __name__ == "__main__":
    print(solve(3))
    print(solve(4))
    print(solve(5))
    print(solve(6))
    print(solve(7))
    ...
