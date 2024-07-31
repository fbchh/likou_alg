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

        _used1 = {}
        for i in range(self._len):
            if used.get(i, 0) == 1:  # 控制子分支上前后不会使用同一索引的元素
                continue
            if _used1.get(arr[i], 0) == 1:  # 控制同一层不会使用同样数值的元素
                continue

            sgl_res.append(arr[i])
            _used1[arr[i]] = 1
            used[i] = 1
            self.core_backtrack(arr, sgl_res, res, used)
            sgl_res.pop()
            used[i] = 0

    def solve(self, tgt_nums):
        self._len = len(tgt_nums)
        res = []
        tgt_nums.sort()
        self.core_backtrack(tgt_nums, [], res, {})
        return res


if __name__ == "__main__":
    tst_ege_nums = [1, 1, 2]
    solve_obj = Solve()
    print(solve_obj.solve(tst_ege_nums))
    print(solve_obj.solve([1, 2, 3]))
