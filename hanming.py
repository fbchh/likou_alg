"""
题目：计算两个数字之间的汉明距离
“汉明距离”：将两个数字转为二进制字符串后，两个字符串相互变换所需要改变的字符个数
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # print(bin(x), bin(y), len(bin(x)))

        str_x = bin(x).split('0b')[1]
        str_y = bin(y).split('0b')[1]
        len_x = len(str_x)
        len_y = len(str_y)
        len_res = len_x - len_y

        str_head = ['0' for i in range(abs(len_res))]
        str_head = ''.join(str_head)
        if len_res > 0:
            str_y = str_head + str_y
        elif len_res < 0:
            str_x = str_head + str_x

        # print(str_x, str_y)
        diff_times = 0
        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                diff_times += 1
        return diff_times


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
