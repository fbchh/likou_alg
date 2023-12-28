"""
题目：最大连续1的个数
题意：给定一个二进制数组，计算其中最大连续1的个数
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        str_nums = "".join([str(e) for e in nums]).split("0")
        arr_times = [len(e) for e in str_nums]
        return max(arr_times)

"""
下面的代码直接遍历输入的数组进行统计，相比与上面的方法而言省去了字符串转换的步骤，减少了开销
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                max_ones = max(max_ones, current_ones)
                current_ones = 0

        return max(max_ones, current_ones)

"""

if __name__ == "__main__":
    class tst1:
        input_nums = [1, 1, 0, 1, 1, 1]
        res = 3


    class tst2:
        input_nums = [1, 0, 1, 1, 0, 1]
        res = 2


    _ = Solution()
    print(_.findMaxConsecutiveOnes(tst1.input_nums))
    print(_.findMaxConsecutiveOnes(tst2.input_nums))
