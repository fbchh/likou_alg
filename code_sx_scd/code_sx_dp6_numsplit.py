"""
xxx
"""


def solve(n):
    dp = [-1, -1, 1]

    idx = 3
    while idx <= n:

        num1 = 1
        sgl_max = -1
        while num1 <= (idx / 2):  # 内循环暴力枚举
            sgl_max = max(sgl_max, dp[idx - num1] * num1, (idx - num1) * num1)
            num1 += 1

        dp.append(sgl_max)
        idx += 1

    return dp[-1]


if __name__ == "__main__":
    print(solve(2))
    print(solve(10))
    ...
