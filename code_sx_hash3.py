"""
代码随想录学习记录
章节：哈希表
题目：快乐数

    题意：

    编写一个算法来判断一个数 n 是不是快乐数。
    「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
    如果 n 是快乐数就返回 True ；不是，则返回 False 。

    示例：

    输入：19
    输出：true
    解释：
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
"""
from time import time, sleep


def count_time(input_func):
    t1 = time()
    input_func()
    print(f"[info] tol cost sec: {time() - t1}S")


def solve1(input_num):
    """
    解法1，官方的思路，判断每次“处理”后的结果，如果在hash中则返回false，否则继续
    :param input_num:xx
    :return:xx
    """
    _hash = {}
    cur_num = input_num
    while 1:
        cur_num = sum([pow(int(e), 2) for e in str(cur_num)])
        if cur_num == 1:
            return True
        else:
            if _hash.get(cur_num) is not None:
                return False
            else:
                _hash[cur_num] = _hash.get(cur_num, 0)


def solve2(input_num):
    """
    解法1的同一种思路，换一种实现方法
    :param input_num:xx
    :return:xx
    """
    _hash = set()
    cur_num = input_num
    while 1:
        cur_num = sum([pow(int(e), 2) for e in str(cur_num)])
        if cur_num == 1:
            return True
        else:
            if cur_num in _hash:
                return False
            else:
                _hash.add(cur_num)


if __name__ == "__main__":

    def tst1():
        print(solve1(2))
    count_time(tst1)

    def tst2():
        print(solve2(2))
    count_time(tst2)

