"""
xxx
"""


class Solve:

    def __init__(self):
        self.nums_len = 0

    def core(self, nums, tgt_num, cur_tol, start_idx, sgl_res, res, used_bool):
        if cur_tol == tgt_num:
            res.append(sgl_res[:])
            return

        for i in range(start_idx, self.nums_len):
            if cur_tol + nums[i] > tgt_num:
                break
            if i > 0 and nums[i] == nums[i - 1] and used_bool[i - 1] is False:
                continue
            cur_tol += nums[i]
            sgl_res.append(nums[i])
            used_bool[i] = True
            self.core(nums, tgt_num, cur_tol, i + 1, sgl_res, res, used_bool)
            cur_tol -= nums[i]
            sgl_res.pop()
            used_bool[i] = False

    def solve(self, candidates, target):
        self.nums_len = len(candidates)
        res = []
        candidates = sorted(candidates)
        self.core(candidates, target, 0, 0, [], res, [False] * self.nums_len)
        return res


if __name__ == "__main__":
    tst_nums = [10, 1, 2, 7, 6, 1, 5]
    tst_tgt_num = 8
    solve_obj = Solve()
    print(solve_obj.solve(tst_nums, tst_tgt_num))
    pass
