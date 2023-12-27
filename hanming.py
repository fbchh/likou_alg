"""
题目：计算两个数字之间的汉明距离
“汉明距离”：将两个数字转为二进制字符串后，两个字符串相互变换所需要改变的字符个数
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    class tst1:
        num1 = 1
        num2 = 4
        res = 2


    class tst2:
        num1 = 1
        num2 = 3
        res = 1


    _ = Solution()
    print(_.hammingDistance(tst1.num1, tst1.num2))
    print(_.hammingDistance(tst2.num1, tst2.num2))
