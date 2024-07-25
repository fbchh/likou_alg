"""
xxx
"""


class Solve:
    def __init__(self):
        self.arr_len = 0

    def core_backtrack(self, arr, start_idx, sgl_res, res):
        res.append(sgl_res[:])

        for i in range(start_idx, self.arr_len):
            sgl_res.append(arr[i])
            self.core_backtrack(arr, i + 1, sgl_res, res)
            sgl_res.pop()

    def solve(self, tgt_nums):
        self.arr_len = len(tgt_nums)
        res = []
        self.core_backtrack(tgt_nums, 0, [], res)
        return res


if __name__ == "__main__":
    tst_ege1_arr = [1, 2, 3]
    solve_obj = Solve()
    print(solve_obj.solve(tst_ege1_arr))

    pass
