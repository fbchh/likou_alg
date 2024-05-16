"""
代码随想录学习记录
章节：数组
题目：螺旋矩阵II

    给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

    示例:
    输入: 3 输出: [  [ 1, 2, 3 ],
                   [ 8, 9, 4 ],
                  [ 7, 6, 5 ] ]
"""


def slove1(input_n):
    """
    解法1：由题意“正方形”矩阵，所以这个矩阵的size就是n*n
    :param input_n: xx
    :return: xx
    """
    _res = [[0] * input_n for _i in range(input_n)]
    _loop_num = input_n // 2 # 循环次数 以一圈为一个“循环”
    l_set = 1 # 左开右闭 “右边”在一圈圈向内的过程中会向着左边缩进
    start_i = 0 # 循环起始元素索引
    start_j = 0
    count_num = 1
    while _loop_num > 0:

        # 上行元素,从左到右
        for i in range(start_j, input_n - l_set):
            _res[start_i][i] = count_num
            count_num += 1

        # 右列元素，从上到下
        for i in range(start_i, input_n - l_set):
            _res[i][input_n - l_set] = count_num
            count_num += 1

        # 下行元素，从右到左
        for i in range(input_n - l_set, start_j, -1):
            _res[input_n - l_set][i] = count_num
            count_num += 1

        # 左列元素，从下到上
        for i in range(input_n - l_set, start_i, -1):
            _res[i][start_j] = count_num
            count_num += 1

        _loop_num -= 1
        start_i += 1
        start_j += 1
        l_set += 1

    if input_n % 2:
        _mid_indx = input_n // 2
        _res[_mid_indx][_mid_indx] = input_n*input_n

    _ = [print(f"{e}\r") for e in _res]

    return _res


def solve2(input_n):
    """
    拓展：其他条件不变，逆时针(简称“左旋”)
    :param input_n:xx
    :return:xx
    """
    _res = [[0] * input_n for _ in range(input_n)]
    loop_num = input_n // 2
    if input_n % 2:
        _res[loop_num][loop_num] = input_n * input_n

    start_i, start_j = 0, input_n - 1
    set_num = 1  # 每圈中“尾部边界的”偏移量
    count_num = 1
    while loop_num > 0:

        # 上行元素，从右到左
        for i in range(start_j, set_num - 1, -1):
            _res[start_i][i] = count_num
            count_num += 1

        # 左列元素，从上到下
        for i in range(start_i, input_n - set_num):
            _res[i][set_num - 1] = count_num
            count_num += 1

        # 下行元素，从左到右
        for i in range(set_num - 1, input_n - set_num):
            _res[input_n - set_num][i] = count_num
            count_num += 1

        # 右列元素，从下到上
        for i in range(input_n - set_num, start_i, -1):
            _res[i][start_j] = count_num
            count_num += 1

        start_i += 1
        start_j -= 1
        loop_num -= 1
        set_num += 1

    _ = [print(f"{e}\r") for e in _res]
    return _res


if __name__ == "__main__":
    from time import time

    t1 = time()

    slove1(3)
    # slove1(4)
    # slove1(12)
    print()

    solve2(3)

    t2 = time()
    print(f"[info] tol cost sec: {t2 - t1}S")
