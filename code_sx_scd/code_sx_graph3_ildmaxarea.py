"""
xxx
"""


class Solve:

    def __init__(self, n=None, m=None, arr=None):
        if None in [n, m, arr]:  # acm mode
            def get_sgl_line_input():
                return map(int, input().split())

            self.n, self.m = get_sgl_line_input()
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = []
            for _ in range(self.n):
                self.arr.append(list(get_sgl_line_input()))
        else:  # tst mode
            self.n, self.m = n, m
            self.arr = arr
            self.matrix = [[False] * self.m for _ in range(self.n)]

        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 顺时针 上、右、下、左
        self.sgl_area = 0

    def dfs(self, cur_node):
        if self.matrix[cur_node[0]][cur_node[1]] or self.arr[cur_node[0]][cur_node[1]] == 0:
            return

        self.matrix[cur_node[0]][cur_node[1]] = True
        self.sgl_area += 1

        for e in self.direct:
            next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
            if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                continue
            self.dfs(next_node)

    def bfs(self, work_nodes):
        while len(work_nodes) > 0:
            cur_node = work_nodes.pop(0)

            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    continue
                if not self.matrix[next_node[0]][next_node[1]] and self.arr[next_node[0]][next_node[1]] == 1:
                    self.matrix[next_node[0]][next_node[1]] = True
                    self.sgl_area += 1
                    work_nodes.append(next_node)

    def solve_main(self, mode=1):
        """
        :param mode: 1--dfs 2--bfs
        :return: num (max area)
        """
        res_area = 0
        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    # 单块岛屿的面积
                    if mode == 1:
                        self.dfs([i, j])
                    if mode == 2:
                        self.matrix[i][j] = True
                        self.sgl_area += 1
                        self.bfs([[i, j]])

                    res_area = max(self.sgl_area, res_area)
                    self.sgl_area = 0
        print(res_area)
        return res_area


if __name__ == "__main__":
    tst_obj = Solve(4, 5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
    tst_obj.solve_main(1)
    ...
