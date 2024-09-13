"""
xxx
"""


def solve(strs, m, n):
    def get_times(input_str):
        zero_times = 0
        one_times = 0
        for e in input_str:
            if e == "0":
                zero_times += 1
            elif e == "1":
                one_times += 1
        return zero_times, one_times

    res = [[0] * (m + 1) for _ in range(n + 1)]

    for e in strs:
        num1, num2 = get_times(e)
        for i in range(n, num2 - 1, -1):
            for j in range(m, num1 - 1, -1):
                res[i][j] = max(res[i][j], 1 + res[i - num2][j - num1])
    return res[-1][-1]


if __name__ == "__main__":
    print(solve(["10", "0001", "111001", "1", "0"], 5, 3))
    print(solve(["10", "0", "1"], 1, 1))
    ...
