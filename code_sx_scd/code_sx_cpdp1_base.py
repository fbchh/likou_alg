"""
xxx
"""


def solve(weights, values, backpack_num):
    res = [0] * (backpack_num + 1)

    for i in range(len(weights)):
        for j in range(weights[i], backpack_num + 1):
            res[j] = max(res[j], values[i] + res[j - weights[i]])

    return res[-1]


if __name__ == "__main__":
    print(solve([1, 3, 4], [15, 20, 30], 4))
    ...
