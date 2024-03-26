"""
代码随想录学习记录
章节：字符串
题目：反转字符串II

    题意：
    给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。
    补充：
        如果剩余字符少于 k 个，则将剩余字符全部反转。
        如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

    示例:
        输入: s = "abcdefg", k = 2
        输出: "bacdfeg"
"""


def sub_solve(s):
    """
    反转字符串II(子方法)
    :param s: xx
    :return: xx
    """
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


def solve1(s, k):
    """
    官方解法，步长设置为2k，然后处理即可,一开始想的比较复杂，官方的补充说明有点让人费解
    :param s: xx
    :param k: xx
    :return: xx
    """
    s = list(s)
    for i in range(0, len(s), 2 * k):  # 自己想的有点复杂，题意中描述的是，每计数2k，就在这新的2k区间内处理，最后才是补充点的处理
        s[i:i + k] = sub_solve(s[i:i + k])
    return ''.join(s)


if __name__ == "__main__":
    """
    python中数组切片说明，start:end 表示中间的所有元素，“左闭右开”原则
    a = [1,2,3,4]
    a[:2] = [1,2] 
    a[1:2] = [2] 
    """
    print(solve1("abcdefg", 2))
    pass
