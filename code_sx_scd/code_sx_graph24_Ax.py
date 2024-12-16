"""
xxx
"""
import heapq


class Solve:

    @staticmethod
    def dist(p1, p2):
        return pow((pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)), 0.5)

    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.n = list(sgl_line_input())[0]
        self.Q = []
        for _ in range(self.n):
            p1_x, p1_y, p2_x, p2_y = sgl_line_input()
            self.Q.append(
                ((p1_x, p1_y), (p2_x, p2_y))
            )
        self.dirct = [[-2, -1], [-2, 1],  # 上
                      [-1, 2], [1, 2],  # 右
                      [2, 1], [2, -1],  # 下
                      [1, -2], [-1, -2]]  # 左

    def sgl_solve(self, p1, p2):
        work_arr = [(self.dist(p1, p2), p1)]
        step_rcd = {p1: 0}  # 记录距离

        while len(work_arr) > 0:
            d, p = heapq.heappop(work_arr)
            if p == p2:
                return step_rcd[p]
            for sgl_dirct in self.dirct:
                new_p = (p[0] + sgl_dirct[0], p[1] + sgl_dirct[1])
                if new_p[0] in [0, 1001] or new_p[1] in [0, 1001]:
                    continue
                new_d = step_rcd[p] + 1
                if new_d < step_rcd.get(new_p, float("inf")):
                    step_rcd[new_p] = new_d
                    heapq.heappush(work_arr, (new_d + self.dist(new_p, p2), new_p))
        return None

    def solve_main(self):
        for p1, p2 in self.Q:  # 单次解答
            print(self.sgl_solve(p1, p2))


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
