"""
xxx
"""


def solve(n):
    dp = [1, 1, 2]

    idx = 3
    while idx <= n:

        num = 1
        tol_kind_num = 0
        while num <= idx:
            tol_kind_num += dp[num - 1] * dp[idx - num]
            num += 1
        dp.append(tol_kind_num)
        idx += 1

    return dp[n]


if __name__ == "__main__":
    print(solve(3))
    print(solve(1))
    print(solve(4))
    ...
