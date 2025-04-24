"""
 @Time: 2025/4/24 10:37
 @Auther: FBC
"""


def xx_tst(nums, func_idx=0):
    """
    nums 整数数组（正负） 最大和的连续子数组 返回最大和
    解法 -> 单调栈（x序）
    暴力：双层循环，外层 -> “起始索引”，内层 -> "结束索引"
    随想录解法1：贪心
    随想录解法2：动规
    """

    def solve1(tgt_nums):
        tgt_nums_len = len(tgt_nums)

        max_count = -pow(10, 15)
        for start_idx in range(tgt_nums_len):
            sgl_count = max_count
            for end_idx in range(start_idx + 1, tgt_nums_len):
                cur_count = sum(tgt_nums[start_idx:end_idx + 1])
                if cur_count > sgl_count:
                    sgl_count = cur_count
            if max_count < sgl_count:
                max_count = sgl_count

        return max_count

    def solve2(tgt_nums):
        # 贪心
        tgt_nums_len = len(tgt_nums)
        max_count = -pow(10, 15)

        sgl_count = 0
        for i in range(tgt_nums_len):
            sgl_count += tgt_nums[i]
            max_count = max(max_count, sgl_count)
            if sgl_count < 0:
                sgl_count = 0
                continue
        return max_count

    def solve3(tgt_nums):
        # 动规
        # i上的子序和取决于i-1

        tgt_nums_len = len(tgt_nums)
        dp = [0] * tgt_nums_len
        dp[0] = tgt_nums[0]

        for i in range(1, tgt_nums_len):
            dp[i] = dp[i - 1] + tgt_nums[i] if dp[i - 1] > 0 else tgt_nums[i]
        return max(dp)

    if func_idx not in list(range(3)):
        func_idx = 0

    func = [solve1, solve2, solve3]

    return func[func_idx](nums)


if __name__ == "__main__":
    tst_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(xx_tst(tst_nums, 2))
