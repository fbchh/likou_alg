"""
代码随想录学习记录
章节：哈希表
题目：四数相加II

    题意：

    给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

    例如:
        输入:
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]
        输出:
        2
        解释:
        两个元组如下:
        (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
        (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


def solve1(arr1, arr2, arr3, arr4):
    """
    解法1，随想录官方思想，将四个数求和的问题转化为两数求和的问题
    :param arr1: xx
    :param arr2: xx
    :param arr3: xx
    :param arr4: xx
    :return: xx
    """
    _record = {}
    _res = 0
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            _record[arr1[i] + arr2[j]] = _record.get(arr1[i] + arr2[j], 0) + 1

    for i in range(len(arr1)):
        for j in range(len(arr1)):
            _res += _record.get(0 - (arr3[i] + arr4[j]), 0)
    return _res


if __name__ == "__main__":

    print(solve1([1, 2],[-2, -1], [-1, 2], [0, 2]))

    print(solve1([-1, -1],[-1, 1], [-1, 1], [1, -1]))
