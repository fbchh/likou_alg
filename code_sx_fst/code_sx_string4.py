"""
代码随想录学习记录
章节：字符串
题目：翻转字符串里的单词

    题意：
    给定一个字符串，逐个翻转字符串中的每个单词。
    示例 1：
        输入: "the sky is blue"
        输出: "blue is sky the"
    示例 2：
        输入: "  hello world!  "
        输出: "world! hello"
        解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    示例 3：
        输入: "a good   example"
        输出: "example good a"
        解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个
"""


def solve1(s):
    """
    解法1，借助内置api方法
    :param s: xx
    :return: xx
    """
    s = s.split()
    s.reverse()
    return ' '.join(s)


def solve2(s):
    """
    手搓版，不使用任何内置方法，双指针大法
    :param s: xx
    :return: xx
    """
    l = r = None
    s = " " + s + " "
    _res = []
    for i in range(len(s)):
        if s[i] != " " and l is None:
            l = r = i
        elif s[i] != " " and l is not None:
            r = i
        elif s[i] == " " and l is not None:
            _res.append(s[l:r + 1])
            l = r = None

    l = 0
    r = len(_res) - 1
    while l < r:
        _res[l], _res[r] = _res[r], _res[l]
        l += 1
        r -= 1

    _res_str = ""
    for e in _res:
        _res_str = _res_str + " " + e
    return _res_str[1:]


if __name__ == "__main__":
    print(solve1("the sky is blue"))
    print(solve1("  hello world!  "))
    print(solve1("a good   example"))

    print(solve2("the sky is blue"))
    print(solve2("  hello world!  "))
    print(solve2("a good   example"))
    pass
