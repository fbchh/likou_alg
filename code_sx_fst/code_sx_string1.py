"""
代码随想录学习记录
章节：字符串
题目：反转字符串

    题意：
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

    示例 1：
        输入：["h","e","l","l","o"]
        输出：["o","l","l","e","h"]
    示例 2：
        输入：["H","a","n","n","a","h"]
        输出：["h","a","n","n","a","H"]
"""


def solve1(str_arr):
    l = 0
    r = len(str_arr) - 1

    while l < r:
        str_arr[l], str_arr[r] = str_arr[r], str_arr[l]  # 跟下面的代码是一样的作用
        # _mid_char = str_arr[l]
        # str_arr[l] = str_arr[r]
        # str_arr[r] = _mid_char
        l += 1
        r -= 1
    return str_arr


if __name__ == "__main__":
    print(solve1(["h", "e", "l", "l", "o"]))
    print(solve1(["H", "a", "n", "n", "a", "h"]))
    pass
