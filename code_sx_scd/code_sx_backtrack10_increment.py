"""
xxx
"""


class Solve:
    def __init__(self):
        self._len = 0

    def core_backtrack(self, arr, start_idx, sgl_res, res):
        if len(sgl_res) >= 2:
            res.append(sgl_res[:])

        used_bool = {}
        for i in range(start_idx, self._len):
            _ = used_bool.get(arr[i], 0)
            if (len(sgl_res) > 0 and arr[i] < sgl_res[-1]) or _ == 1:
                continue

            used_bool[arr[i]] = 1
            sgl_res.append(arr[i])
            self.core_backtrack(arr, i + 1, sgl_res, res)
            sgl_res.pop()

    def solve(self, tgt_nums):
        self._len = len(tgt_nums)
        res = []
        self.core_backtrack(tgt_nums, 0, [], res)
        return res


if __name__ == "__main__":
    tst_ege_nums = [4, 6, 7, 7]
    solve_obj = Solve()
    print(solve_obj.solve(tst_ege_nums))
    ...
