"""
xxx
"""


class Solve:
    def __init__(self):
        self.tgt_len = 0

    def core_backtrack(self, arr, start_idx, used, sgl_res, res):
        res.append(sgl_res[:])

        for i in range(start_idx, self.tgt_len):
            if i > 0 and arr[i - 1] == arr[i] and used[i - 1] == 0:
                continue

            sgl_res.append(arr[i])
            used[i] = 1
            self.core_backtrack(arr, i + 1, used, sgl_res, res)
            sgl_res.pop()
            used[i] = 0

    def solve(self, tgt_nums):
        self.tgt_len = len(tgt_nums)
        res = []
        tgt_nums.sort()
        self.core_backtrack(tgt_nums, 0, [0] * self.tgt_len, [], res)
        return res


if __name__ == "__main__":
    tst_ege_nums1 = [1, 2, 2]
    solve_obj = Solve()
    print(solve_obj.solve(tst_ege_nums1))

    ...
