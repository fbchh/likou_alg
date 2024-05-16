"""
代码随想录学习记录
章节：字符串
题目：重复的字符串

    题意：
    给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
    示例 1:
        输入: "abab"
        输出: True
        解释: 可由子字符串 "ab" 重复两次构成。
    示例 2:
        输入: "aba"
        输出: False
    示例 3:
        输入: "abcabcabcabc"
        输出: True
        解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
"""


def solve1(s):
    """
    解法1，先循环遍历是否存在相同元素i和0对比，相同则截取子串对比，子串相同，则对比子串长度和总长度之间的倍数关系，呈倍数关系则判断后续子串是否相同
    :param s: xx
    :return: xx
    """
    _s = list(s)
    _s_head = _s[0]
    for i in range(1, len(_s)):
        if _s[i] == _s_head:
            _s_l = _s[0:i]
            _s_r = _s[i:2 * i]
            _num = len(_s) / i
            if _s_l == _s_r and int(_num) == _num and len(set(s.split(''.join(_s_l)))) == 1:
                return True
    return False


def solve2(s):
    """
    解法2，截取原字符串的子串组成新的字符串，在新的字符串中find原来的串（随想录官方记载的一种“移动匹配法”）
    :param s: xx
    :return: xx
    """
    if len(s) <= 1:
        return False
    _res = (s[1:] + s[:-1]).find(s)
    return True if _res != -1 else False


def solve3(s):
    """
    解法3，kmp，细节见随想录，这里没有细看了
    :param s:
    :return:
    """
    pass


if __name__ == "__main__":
    print(solve1("abab"))
    print(solve1("aba"))
    print(solve1("abcabcabcabc"))
    print(solve1("ababba"))
    print(solve1("aabaaba"))

    print("\r")
    print(solve2("abab"))
    print(solve2("aba"))
    print(solve2("abcabcabcabc"))
    print(solve2("ababba"))
    print(solve2("aabaaba"))
    pass
