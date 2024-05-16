"""
代码随想录学习记录
章节：字符串
题目：实现strStr()函数

    题意：
    实现 strStr() 函数。

    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

    示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

    示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

    说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
    对于本题而言，当 needle 是空字符串时我们应当返回 0 。
    这与C语言的 strstr() 以及 Java的 indexOf() 定义相符
"""


def solve1(s1, s2):
    """
    解法1，“水题”
    :param s1: xx
    :param s2: xx
    :return: xx
    """
    return s1.find(s2)


def solve2(s1, s2):
    """
    解法2，循环检测，如果当前元素于指定字符串的第一个元素相同，截取子串进行对比（随想录官方有更优解法，此解法<简称滑窗>不再实现）
    :param s1: xx
    :param s2: xx
    :return: xx
    """
    pass


def solve3(s1, s2):
    """
    解法3，kmp
    :param s1:
    :param s2:
    :return:
    """

    def get_next(input_s):
        """
        构建前缀表，随想录官方思想的实现
        :param input_s: xx
        :return: xx
        """
        _s = list(input_s)
        _res = [0] * len(_s)
        _res[0] = -1

        j = -1
        for i in range(1, len(_s)):
            if _s[i] == _s[j + 1]:
                j += 1
            while j >= 0 and _s[i] == _s[j + 1]:
                j = _res[j]
            _res[i] = j
        return _res

    def main(input_s1, input_s2):
        _res = get_next(input_s2)
        j = -1
        for i in range(len(input_s1)):
            while input_s1[i] != input_s2[j + 1] and j >= 0:
                j = _res[j]
                pass
            if input_s1[i] == input_s2[j + 1]:
                j += 1
            if j == len(input_s2) - 1:
                return i - len(input_s2) + 1
        return -1

    return main(s1, s2)


def pre_deal(s):
    """
    前缀表实现，这是没有参考算法随想录关于前缀表的实现思想前的实现，可以看到，处理思想是左指针相向移动，而随想录官方的思想是同时向后遍历
    :param s: xx
    :return: xx
    """
    s = list(s)
    _res = [0] * len(s)
    for i in range(1, len(s)):
        _count = 0
        _sub = s[:i+1]
        l = 0
        r = len(_sub) - 1
        while l < len(_sub) - 1:
            if _sub[:l+1] == _sub[r:]:
                _count += 1
                l += 1
                r -= 1
            else:
                break
        _res[i] = _count
    return _res


if __name__ == "__main__":
    print(solve1("hello", "ll"))
    print(solve3("hello", "ll"))

    print(solve1("aaaaa", "bba"))
    print(solve3("aaaaa", "bba"))
    pass
