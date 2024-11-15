"""
xxx
"""


class Solve:

    def __init__(self, n=None, m=None, arr=None):
        if None in [n, m, arr]:
            def sgl_line_input():
                return map(int, input().split())

            self.n, self.m = sgl_line_input()
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = []
            for _ in range(self.n):
                self.arr.append(list(sgl_line_input()))

        else:
            self.n, self.m = n, m
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = arr
        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 顺时针方向
        self.sgl_area = 0
        self.is_alone_ild = False

    def dfs(self, cur_node):
        if self.matrix[cur_node[0]][cur_node[1]] or self.arr[cur_node[0]][cur_node[1]] == 0:
            return
        self.matrix[cur_node[0]][cur_node[1]] = True
        self.sgl_area += 1

        for e in self.direct:
            next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
            if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                self.is_alone_ild = True
                continue
            self.dfs(next_node)

    def bfs(self, work_nodes):
        while len(work_nodes) > 0:
            cur_node = work_nodes.pop(0)

            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    self.is_alone_ild = True
                    continue
                if not self.matrix[next_node[0]][next_node[1]] and self.arr[next_node[0]][next_node[1]] == 1:
                    self.matrix[next_node[0]][next_node[1]] = True
                    self.sgl_area += 1
                    work_nodes.append(next_node)

    def solve_main(self, mode=1):
        """
        入口方法
        :param mode: 1--dfs 2--bfs
        """
        alone_ild_area = 0
        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    if mode == 1:
                        self.dfs([i, j])
                    elif mode == 2:
                        self.matrix[i][j] = True
                        self.sgl_area += 1
                        self.bfs([[i, j]])
                    alone_ild_area += self.sgl_area if not self.is_alone_ild else 0
                    self.sgl_area = 0
                    self.is_alone_ild = False

        print(alone_ild_area)
        return alone_ild_area


if __name__ == "__main__":
    # tst_obj = Solve(4, 5, [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 0, 1, 1]
    # ])
    # tst_obj.solve_main(2)

    tst_obj = Solve(10, 10, [
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 0]
    ])
    tst_obj.solve_main(1)
    ...
