"""
xxx
"""


def solve(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
        return 1

    res = [[e1 for e1 in e] for e in obstacleGrid]
    res[0][0] = -1  # 初始化的小细节 不要和做判定的目标值设定一致
    for i in range(1, len(obstacleGrid[0])):
        res[0][i] = 0 if obstacleGrid[0][i] == 1 or res[0][i - 1] == 0 else 1
    for i in range(1, len(res)):  # 这里的逻辑可以放到下面的双层循环中 减少一个循环
        res[i][0] = 0 if obstacleGrid[i][0] == 1 or res[i - 1][0] == 0 else 1

    for i in range(len(res)):
        for j in range(len(res[i])):
            if i != 0 and j != 0:
                res[i][j] = res[i - 1][j] + res[i][j - 1] if res[i][j] != 1 else 0

    return res[-1][-1]


if __name__ == "__main__":
    print(solve(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ))
    print(solve(
        [[0, 1], [0, 0]]
    ))
    ...
