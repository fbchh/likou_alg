"""
xxx
"""


def solve(stones):
    backpack_max_num = int(sum(stones) / 2)

    res = [0 for _ in range(backpack_max_num + 1)]
    for i in range(1, len(res)):
        if i >= stones[0]:
            res[i] = stones[0]

    for i in range(1, len(stones)):
        for j in range(len(res) - 1, 0, -1):
            if j >= stones[i]:
                res[j] = max(res[j], stones[i] + res[j - stones[i]])

    return sum(stones) - 2 * res[-1]


if __name__ == "__main__":
    print(solve([2, 7, 4, 1, 8, 1]))
    ...

"""
递归五部曲：
    1.明确dp数组以及dp[i]的含义
    2.明确递推公式
    3.明确初始化方式
    4.明确遍历方式
    5.举例推导
"""
