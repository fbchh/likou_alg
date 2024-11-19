"""
xxx
"""


class ParamParse:
    def __init__(self):
        # 参数传递

        self.n, self.m = self.sgl_line_input()
        self.arr = []
        for _ in range(self.n):
            self.arr.append(list(self.sgl_line_input()))

    @staticmethod
    def sgl_line_input():
        return map(int, input().split())


class Solve(ParamParse):

    def __init__(self, n=None, m=None, arr=None):
        if None in [n, m, arr]:
            super().__init__()
        else:
            self.n, self.m = n, m
            self.arr = arr
        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.matrix1 = [[False] * self.m for _ in range(self.n)]  # 边界1遍历记录
        self.matrix2 = [[False] * self.m for _ in range(self.n)]  # 边界2遍历记录

    def dfs(self, cur_node, tgt_matrix):
        if tgt_matrix[cur_node[0]][cur_node[1]]:
            return
        tgt_matrix[cur_node[0]][cur_node[1]] = True

        for e in self.direct:
            next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
            if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                continue

            if self.arr[next_node[0]][next_node[1]] >= self.arr[cur_node[0]][cur_node[1]]:
                self.dfs(next_node, tgt_matrix)

    def bfs(self, work_nodes, tgt_matrix):
        while len(work_nodes):
            cur_node = work_nodes.pop(0)

            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    continue
                if not tgt_matrix[next_node[0]][next_node[1]] and self.arr[next_node[0]][next_node[1]] >= \
                        self.arr[cur_node[0]][cur_node[1]]:
                    tgt_matrix[next_node[0]][next_node[1]] = True
                    work_nodes.append(next_node)

    def res_prt(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix1[i][j] and self.matrix2[i][j]:
                    print(str(i) + " " + str(j))

    def solve_main(self, mode=1):
        """
        mode 1--dfs、2--bfs
        """
        # 边界1、2搜索
        for i in range(self.n):
            for j in range(self.m):
                if (i == 0 or j == 0) and not self.matrix1[i][j]:  # 边界1 上、左
                    if mode == 1:
                        self.dfs([i, j], self.matrix1)
                    elif mode == 2:
                        self.matrix1[i][j] = True
                        self.bfs([[i, j]], self.matrix1)

        for i in range(self.n):
            for j in range(self.m):
                if (i == self.n - 1 or j == self.m - 1) and not self.matrix2[i][j]:  # 边界2 下、右
                    if mode == 1:
                        self.dfs([i, j], self.matrix2)
                    elif mode == 2:
                        self.matrix2[i][j] = True
                        self.bfs([[i, j]], self.matrix2)

        # 结果1、2输出
        self.res_prt()


if __name__ == "__main__":
    tst_obj = Solve(5, 5, [
        [1, 3, 1, 2, 4],
        [1, 2, 1, 3, 2],
        [2, 4, 7, 2, 1],
        [4, 5, 6, 1, 1],
        [1, 4, 1, 2, 1]
    ])
    tst_obj.solve_main(2)
    ...
