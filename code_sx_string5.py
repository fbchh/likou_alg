"""
代码随想录学习记录
章节：字符串
题目：右旋转字符串

    题意：
    字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。
    例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。
    输入：
        输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。
    输出：
        输出共一行，为进行了右旋转操作后的字符串
"""


def solve1(s, k):
    """
    解法1，“水题”做法
    :param s: xx
    :param k: xx
    :return: xx
    """
    return s[-k:] + s[:-k]


def solve2(s, k):
    """
    解法2，先整体翻转，再局部翻转
    :param s: xx
    :param k: xx
    :return: xx
    """
    def sub_deal(_s):
        l = 0
        r = len(_s) - 1
        while l < r:
            _s[l], _s[r] = _s[r], _s[l]
            l += 1
            r -= 1
        return _s
    s = list(s)
    s = sub_deal(s)
    s = sub_deal(s[:k]) + sub_deal(s[k:])
    return ''.join(s)


if __name__ == "__main__":
    print(solve1("abcdefg", 2))
    print(solve2("abcdefg", 2))
    pass
