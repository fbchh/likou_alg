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
        self.matrix = [[False] * self.m for _ in range(self.n)]
        self.sgl_area = 0

    def dfs(self, cur_node, ild_tag_num):
        if self.matrix[cur_node[0]][cur_node[1]] or self.arr[cur_node[0]][cur_node[1]] == 0:
            return
        self.matrix[cur_node[0]][cur_node[1]] = True
        self.arr[cur_node[0]][cur_node[1]] = ild_tag_num
        self.sgl_area += 1

        for e in self.direct:
            next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
            if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                continue
            self.dfs(next_node, ild_tag_num)

    def bfs(self, work_nodes, ild_tag_num):
        while len(work_nodes):
            cur_node = work_nodes.pop(0)

            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    continue

                if not self.matrix[next_node[0]][next_node[1]] and self.arr[next_node[0]][next_node[1]] == 1:
                    self.sgl_area += 1
                    self.arr[next_node[0]][next_node[1]] = ild_tag_num
                    self.matrix[next_node[0]][next_node[1]] = True
                    work_nodes.append(next_node)

    def solve_main(self, mode=1):
        """
        mode 1--dfs 2--bfs
        """
        inner_dict = {}

        # 搜索 标记 统计面积
        key = -1
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 1 and not self.matrix[i][j]:
                    if mode == 1:
                        self.dfs([i, j], key)
                    elif mode == 2:
                        self.matrix[i][j] = True
                        self.sgl_area += 1
                        self.arr[i][j] = key
                        self.bfs([[i, j]], key)
                    inner_dict[key] = self.sgl_area
                    self.sgl_area = 0
                    key -= 1

        # 遍历 比较
        res_area = inner_dict.get(-1, 0)  # 以第一个岛面积为起始面积
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 0:
                    ild_tags = set()
                    for e in self.direct:
                        sgl_idx = [i + e[0], j + e[1]]
                        if sgl_idx[0] in [-1, self.n] or sgl_idx[1] in [-1, self.m]:
                            continue
                        ild_tag = self.arr[sgl_idx[0]][sgl_idx[1]]
                        if ild_tag == 0:
                            continue
                        ild_tags.add(ild_tag)
                    ild_tags = list(ild_tags)
                    sgl_area = 1
                    for e in ild_tags:
                        sgl_area += inner_dict.get(e, 0)
                    res_area = max(res_area, sgl_area)

        # 输出
        print(res_area)
        return res_area


if __name__ == "__main__":
    tst_obj = Solve(4, 5, [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ])
    tst_obj.solve_main(2)

    ...
