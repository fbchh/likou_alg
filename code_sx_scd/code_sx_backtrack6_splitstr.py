"""
xxx
"""


class Solve:
    # 基础版本——未优化前

    def __init__(self):
        self.tgt_str_len = 0

    def core_backtrack(self, input_str, start_idx, sgl_res, res):
        if start_idx == self.tgt_str_len:
            res.append(sgl_res[:])
            return

        for i in range(start_idx, self.tgt_str_len):
            # 处理逻辑
            sub_str = input_str[start_idx:i + 1]
            if self.core_is_tgt_str(sub_str) is True:
                sgl_res.append(sub_str)
            else:
                continue

            self.core_backtrack(input_str, i + 1, sgl_res, res)
            sgl_res.pop()

    @staticmethod
    def core_is_tgt_str(input_str):
        # 这是可以优化的地方
        if len(input_str) == 1:
            return True

        l, r = 0, len(input_str) - 1
        while l < r:
            if input_str[l] != input_str[r]:
                return False
            l += 1
            r -= 1
        return True

    @staticmethod
    def core_is_tgt_str1(input_str):
        _ = list(input_str)
        _.reverse()
        return input_str == "".join(_)

    def solve(self, tgt_str):
        self.tgt_str_len = len(tgt_str)
        res = []
        self.core_backtrack(tgt_str, 0, [], res)
        return res


if __name__ == "__main__":
    tst_str = "aaaaa"
    solve_obj = Solve()
    # print(solve_obj.solve(tst_str))

    print(Solve.core_is_tgt_str1("aba"))
    print(Solve.core_is_tgt_str1("ccca"))
    pass
