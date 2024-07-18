"""
xxx
"""


class Solve:
    def __init__(self):
        self.key_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

    def back_track(self, num_str, cur_idx, sgl_str, res, tgt_len):
        if len(sgl_str) == tgt_len:
            res.append("".join(sgl_str[:]))
            return

        tgt_key_str = self.key_map[int(num_str[cur_idx])]
        for i in range(len(tgt_key_str)):
            sgl_str.append(tgt_key_str[i])
            self.back_track(num_str, cur_idx + 1, sgl_str, res, tgt_len)
            sgl_str.pop()

    def solve(self, digits):
        if digits == "":
            return []
        res = []
        self.back_track(digits, 0, [], res, len(digits))
        return res


if __name__ == "__main__":

    tst_ege1_str = "23"
    tst_ege2_str = "2"
    tst_ege3_str = ""
    solve = Solve()
    # print(solve.solve(tst_ege1_str))
    # print(solve.solve(tst_ege2_str))
    print(solve.solve("4654576347456745674567456745673"))
    pass
