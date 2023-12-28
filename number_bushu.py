"""
题目：数字的补数
理解题意：，转回十进制输出
"""


class Solution:
    def findComplement(self, num: int) -> int:
        _str = bin(num).split('0b')[1]
        _str = ["0" if e == "1" else "1" for e in _str]
        _str = "".join(_str)
        return int(_str, 2)


"""
一种更为简单的做法，如果使用上面基于字符串的方法，在数字较大的时候处理较慢，这里的做法是基于位运算
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) + 1
        return num ^ mask
"""

if __name__ == "__main__":
    class tst1:
        input = 5
        res = 2


    class tst2:
        input = 1
        res = 0


    _ = Solution()
    print(_.findComplement(tst1.input))
    print(_.findComplement(tst2.input))
