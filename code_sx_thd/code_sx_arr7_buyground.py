"""
xxx
"""


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().split())

        n, m = sgl_line_input()
        line_sum = []  # 行求和
        last_line_sum = 0

        col_sum = [0] * m  # 列求和
        for _ in range(n):
            sgl_line = list(sgl_line_input())
            new_line_sum = last_line_sum + sum(sgl_line)
            line_sum.append(new_line_sum)
            last_line_sum = new_line_sum

            las_num = 0
            for i in range(m):
                sgl_line[i] += las_num
                las_num = sgl_line[i]
                col_sum[i] += sgl_line[i]

        res_diff = float("inf")
        tol_matrix = line_sum[-1]
        for e in line_sum:
            res_diff = min(res_diff, abs(e - tol_matrix + e))

        for e in col_sum:
            res_diff = min(res_diff, abs(e - tol_matrix + e))
        self.res = res_diff

    def get_res(self):
        print(self.res)


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.get_res()
    ...
