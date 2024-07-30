"""
xxx
"""


class Solve:

    def __init__(self):
        self._len = 0

    def core_backtrack(self, arr, sgl_res, res, used):
        if len(sgl_res) == self._len:
            res.append(sgl_res[:])
            return

        for i in range(self._len):
            if used.get(arr[i], 0) == 1:
                continue
            sgl_res.append(arr[i])
            used[arr[i]] = 1
            self.core_backtrack(arr, sgl_res, res, used)
            sgl_res.pop()
            used[arr[i]] = 0

    def solve(self, tgt_nums):
        self._len = len(tgt_nums)
        res = []
        self.core_backtrack(tgt_nums, [], res, {})
        return res


if __name__ == "__main__":
    tst_ege_nums = [1, 2, 3]
    solve_obj = Solve()
    print(solve_obj.solve(tst_ege_nums))
    print(solve_obj.solve([0, 1]))
    print(solve_obj.solve([1]))
