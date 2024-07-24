"""
xxx
"""


class Solve:

    def __init__(self):
        self.str_len = 0
        ...

    @staticmethod
    def core_substr_verify(input_str):
        if len(input_str) == 0:
            return False

        if input_str[0] == "0" and len(input_str) > 1:
            return False

        for i in range(len(input_str)):
            if input_str[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                return False

        if int(input_str) > 255:
            return False

        return True

    def core(self, tgt_str, start_idx, add_point_num, sgl_str, res):
        if add_point_num == 3:
            _ = tgt_str[start_idx:]
            if self.core_substr_verify(_):
                sgl_str += _
                res.append(sgl_str)
            return

        for i in range(start_idx, self.str_len):
            _ = tgt_str[start_idx: i + 1]
            if self.core_substr_verify(_) is True:
                self.core(tgt_str, i + 1, add_point_num + 1, sgl_str + _ + '.', res)
            else:
                break

    def solve(self, input_str):
        self.str_len = len(input_str)
        res = []
        self.core(input_str, 0, 0, "", res)
        return res


if __name__ == "__main__":
    tst_str = "25525511135"
    solve_obj = Solve()
    # print(solve_obj.solve(tst_str))
    # print(solve_obj.solve("0000"))
    print(solve_obj.solve("101023"))
    pass
