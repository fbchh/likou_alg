"""
代码随想录学习记录
章节：哈希表
题目：赎金信

    题意：
    给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
    (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
    注意：
    你可以假设两个字符串均只含有小写字母。
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""


def solve1(str1, str2):
    """
    解法1，先把str2中的元素建立哈希结构，然后在遍历str1的时候判断哈希元素是否存在，不存在则返回 False
    :param str1:xx
    :param str2:xx
    :return:xx
    """
    _record = {}
    for e in str2:
        _record[e] = _record.get(e, 0) + 1

    for e in str1:
        if _record.get(e,0) == 0:
            return False
        else:
            _record[e] = _record.get(e) - 1
    return True


def solve2(str1, str2):
    """
    解法2,根据特殊条件“你可以认为只有小写字母”，可以直接构建长度为26的list，占用更少的空间
    :param str1:xx
    :param str2:xx
    :return:xx
    """
    _record = [0] * 26
    for e in str2:
        _record[ord(e) - ord('a')] += 1

    for e in str1:
        if _record[ord(e) - ord('a')] == 0:
            return False
        else:
            _record[ord(e) - ord('a')] -= 1
    return True


if __name__ == "__main__":

    print(solve1("a", "ab"))
    print(solve1("aa", "ab"))
    print(solve1("aa", "aab"))

    print(solve2("a", "ab"))
    print(solve2("aa", "ab"))
    print(solve2("aa", "aab"))
