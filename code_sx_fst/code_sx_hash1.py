"""
代码随想录学习记录
章节：哈希表
题目：有效的字母异位词

    题意：

    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

    示例 2: 输入: s = "rat", t = "car" 输出: false

    说明: 你可以假设字符串只包含小写字母。
"""


def solve1(s, t):
    """
    官方解法，构建一个定长的list，将会出现的字符映射到list中的index，对s遍历，数组元素+1，对t遍历，数组元素-1，最后求和判断即可
    :param s: xx
    :param t: xx
    :return: xx
    """
    _list_set = [0] * 26
    for e in s:
        _list_set[ord(e) - 97] += 1

    for e in t:
        _list_set[ord(e) - 97] -= 1

    return False if len(set(_list_set)) > 1 else True  # 返回逻辑这里卡了很长时间，如果拆分到循环中应该会好一点


if __name__ == "__main__":
    s1 = 'anagram'
    t1 = 'nagaram'
    print(solve1(s1, t1))

    s1 = 'rat'
    t1 = 'car'
    print(solve1(s1, t1))

    s1 = 'a'
    t1 = 'ab'
    print(solve1(s1, t1))

    s1 = 'aa'
    t1 = 'bb'
    print(solve1(s1, t1))
