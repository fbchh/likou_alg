"""
(*)
"""


def solve(weights, values, backpack_max_weight):
    res = [[0 for _1 in range(backpack_max_weight + 1)] for _ in range(len(weights))]
    for i in range(1, len(res[0])):
        if weights[0] <= i:
            res[0][i] = values[0]

    for i in range(1, len(res)):
        for j in range(1, len(res[i])):
            res[i][j] = res[i - 1][j]

            if weights[i] < j:
                res[i][j] = max(res[i][j], values[i] + res[i - 1][j - weights[i]])
            elif weights[i] == j:
                res[i][j] = max(res[i][j], values[i])

    return res[-1][-1]


def solve1(weights, values, backpack_max_weight):
    res = [0 for _1 in range(backpack_max_weight + 1)]
    for i in range(1, len(res)):
        if weights[0] <= i:
            res[i] = values[0]

    for i in range(1, len(weights)):
        for j in range(len(res) - 1, 0, -1):
            if weights[i] < j:
                res[j] = max(res[j], values[i] + res[j - weights[i]])
            elif weights[i] == j:
                res[j] = max(res[j], values[i])

    return res[-1]


if __name__ == "__main__":
    print(solve([1, 3, 4], [15, 20, 30], 4))
    print(solve([1, 3, 2, 4], [20, 50, 32, 27], 5))

    print(solve1([1, 3, 4], [15, 20, 30], 4))
    print(solve1([1, 2, 3, 4], [20, 50, 32, 27], 5))
    ...
