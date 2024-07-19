"""
xxx
"""


class Solve:
    def __init__(self):
        self._len = 0

    def back_trace(self, nums, tol, cur_count, start_idx, sgl_res, res):
        # if cur_count > tol:  # 优化
        #     return

        if cur_count == tol:
            res.append(sgl_res[:])
            return

        for i in range(start_idx, self._len):
            if cur_count + nums[i] > tol:
                break
            cur_count += nums[i]
            sgl_res.append(nums[i])
            self.back_trace(nums, tol, cur_count, i, sgl_res, res)
            cur_count -= nums[i]
            sgl_res.pop()

    def solve(self, candidates: list, target: int):
        self._len = len(candidates)
        res = []
        candidates.sort()
        self.back_trace(candidates, target, 0, 0, [], res)
        return res


if __name__ == "__main__":
    tst_ege1 = [2, 3, 6, 7]
    s_obj = Solve()
    print(s_obj.solve(tst_ege1, 7))

    print(s_obj.solve([2, 3, 5], 8))
    pass

"""
[,[3,3,3,6],[3,3,9],[3,3,5,4],[3,12],[3,6,6],[3,7,5],[3,8,4],[3,4,4,4],[9,6],[11,4],[6,5,4],[7,8],[7,4,4],[5,5,5]]

[[3,4,8],[4,1,1],[3,5,7],[4,5,6],[6,9],[3,1,2],[5,5,5],[3,3,9],[3,4,4,4],[3,6,6],,[3,3,4,5],[3,3,3,6],[4,4,7],[7,8]]
"""
