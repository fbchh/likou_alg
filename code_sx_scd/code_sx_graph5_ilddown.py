"""
xxx
"""


class ParamParse:
    def __init__(self):
        # 参数传递

        self.n, self.m = self.sgl_line_input()
        self.matrix = [[False] * self.m for _ in range(self.n)]
        self.arr = []
        for _ in range(self.n):
            self.arr.append(list(self.sgl_line_input()))

    @staticmethod
    def sgl_line_input():
        return map(int, input().split())


class Solve(ParamParse):
    # 自己的思路：根据每次dfs或者bfs的状态（孤岛还是大陆）以及单次搜索过程中的位置列表沉没孤岛

    def __init__(self, n=None, m=None, arr=None):
        if None in [n, m, arr]:
            super().__init__()
        else:
            self.n, self.m = n, m
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = arr
        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.sgl_idx = []
        self.is_alone_ild = False

    def dfs(self, cur_node):
        if self.matrix[cur_node[0]][cur_node[1]] or self.arr[cur_node[0]][cur_node[1]] == 0:
            return

        self.matrix[cur_node[0]][cur_node[1]] = True
        self.sgl_idx.append(cur_node)

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
                    work_nodes.append(next_node)
                    self.matrix[next_node[0]][next_node[1]] = True
                    self.sgl_idx.append(next_node)

    def down_alone_ild(self):
        for e in self.sgl_idx:
            self.arr[e[0]][e[1]] = 0

    def std_prt(self):
        res_str = ""
        for i in range(self.n - 1):
            sgl_row = " ".join([str(char_s) for char_s in self.arr[i]])
            res_str += f"{sgl_row}\r\n"
        res_str += " ".join([str(char_s) for char_s in self.arr[-1]])
        print(res_str)

    def solve_main(self, mode=1):
        """
        mode 1--dfs, 2--bfs
        """
        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    if mode == 1:
                        self.dfs([i, j])
                    elif mode == 2:
                        self.matrix[i][j] = True
                        self.sgl_idx.append([i, j])
                        self.bfs([[i, j]])

                    if not self.is_alone_ild:
                        self.down_alone_ild()
                    self.sgl_idx = []
                    self.is_alone_ild = False

        self.std_prt()
        return self.arr


class Solve1(Solve):
    # 随想录官方的思路：先将边界上的岛屿处理为“other”，然后沉岛，最后将“other”修改为“陆地”--1

    def dfs(self, cur_node):
        if self.matrix[cur_node[0]][cur_node[1]] or self.arr[cur_node[0]][cur_node[1]] == 0:
            return

        self.matrix[cur_node[0]][cur_node[1]] = True
        self.arr[cur_node[0]][cur_node[1]] = cur_node[2]

        for e in self.direct:
            next_node = [cur_node[0] + e[0], cur_node[1] + e[1], cur_node[2]]
            if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                continue

            self.dfs(next_node)

    def bfs(self, work_nodes):
        while len(work_nodes) > 0:
            cur_node = work_nodes.pop(0)

            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1], cur_node[2]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    continue
                if not self.matrix[next_node[0]][next_node[1]] and self.arr[next_node[0]][next_node[1]] == 1:
                    work_nodes.append(next_node)
                    self.matrix[next_node[0]][next_node[1]] = True
                    self.arr[next_node[0]][next_node[1]] = next_node[2]

    def solve_main(self, mode=1, other_num=2):
        # 1 -> 'other'
        for i in range(self.n):
            for j in range(self.m):
                if (0 < i < self.n - 1) and (0 < j < self.m - 1):
                    continue
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    if mode == 1:
                        self.dfs([i, j, other_num])
                    elif mode == 2:
                        self.matrix[i][j] = True
                        self.arr[i][j] = other_num
                        self.bfs([[i, j, other_num]])

        # alone 1 -> "down"
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 1:
                    self.arr[i][j] = 0

        # 'other' -> 1
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == other_num:
                    self.arr[i][j] = 1

        self.std_prt()


if __name__ == "__main__":
    # tst_obj = Solve(4, 5, [
    #     [1, 1, 0, 0, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 0, 1, 1]
    # ])
    # tst_obj.solve_main(2)

    tst_obj = Solve1(4, 5, [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ])
    tst_obj.solve_main(2)
    ...
