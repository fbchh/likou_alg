"""
题目：密钥格式化
理解题意：将原先的字符串按照要求格式化为新的字符串
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        str_s = s.replace("-", "").upper()
        res_str_head_len = len(str_s) % k
        res_head = str_s[:res_str_head_len]
        str_s = str_s[res_str_head_len:]
        str_s = [str_s[i * k:i * k + k] for i in range(len(str_s) // k)]
        return "-".join([res_head] + str_s) if res_head else "-".join(str_s)


if __name__ == "__main__":
    class tst1:
        input_str = "5F3Z-2e-9-w"
        input_k = 4
        res_str = "5F3Z-2E9W"


    class tst2:
        input_str = "2-5g-3-J"
        input_k = 2
        res_str = "2-5G-3J"


    _ = Solution()
    print(_.licenseKeyFormatting(tst1.res_str, tst1.input_k))
    print(_.licenseKeyFormatting(tst2.res_str, tst2.input_k))
