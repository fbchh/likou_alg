"""
xxx
"""


def solve(gas, cost):
    tol = 0
    count = 0
    idx = 0

    for i in range(len(gas)):
        tol += gas[i] - cost[i]
        count += gas[i] - cost[i]
        if count < 0:
            count = 0
            idx = i + 1
    if tol < 0:
        return -1

    return idx


"""
        if sum(gas) - sum(cost) < 0:
            return -1

        _ = [gas[i] - cost[i] for i in range(len(gas))]
        count = 0
        idx = 0
        for i in range(len(gas)):
            count += _[i]
            if count < 0:
                count = 0
                idx = i + 1
        return idx
"""

if __name__ == "__main__":
    print(solve([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(solve([2, 3, 4], [3, 4, 3]))
    ...
