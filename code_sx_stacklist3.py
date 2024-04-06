"""
代码随想录学习记录
章节：栈和队列
题目：有效的括号

    题意：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

    有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。
    示例 1:
        输入: "()"
        输出: true
    示例 2:
        输入: "()[]{}"
        输出: true
    示例 3:
        输入: "(]"
        输出: false
    示例 4:
        输入: "([)]"
        输出: false
    示例 5:
        输入: "{[]}"
        输出: true
"""


def solve1(s):
    """
    解法1，字典哈希
    :param s: xx
    :return: xx
    """
    a = {}
    for e in list(s):
        a[e] = a.get(e, 0) + 1
    if a.get('(', 0) == a.get(')', 0) and a.get('[', 0) == a.get(']', 0) and a.get('{', 0) == a.get('}', 0):
        return True
    else:
        return False


def solve2(s):
    """
    解法2，随想录官方推荐解法，使用栈处理对称的问题，将左半对应的右半push到栈中，然后再对比目标中的右半，
        具体参考官方，注意其中python版本同时使用数组和字典，这里不在做实现
    :param s: xx
    :return: xx
    """
    pass


if __name__ == "__main__":
    print(solve1("()"))
    print(solve1("()[]{}"))
    print(solve1("(]"))
    print(solve1("{[]}"))
    pass
