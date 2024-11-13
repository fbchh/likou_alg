"""
acm
"""


# dfs版本
class Solve:

    def __init__(self, n=None, m=None, input_arr=None):
        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 方向设置顺时针 上右下左（上下左右这么设置方向会有坑，就顺时针或者逆时针）
        self.res = 0
        if None not in [n, m, input_arr]:
            # 参数传递
            self.n, self.m = n, m
            self.arr = input_arr
            self.matrix = [[False] * self.m for _ in range(self.n)]  # 二维数组（用作记录是否遍历过当前元素）

        else:
            # acm input
            def get_line_input():
                return map(int, input().split())

            self.n, self.m = get_line_input()
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = []
            for i in range(self.n):
                sgl_input = get_line_input()
                self.arr.append(list(sgl_input))

    def dfs(self, cur_node):
        for e in self.direct:
            new_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
            if new_node[0] not in [-1, self.n] and new_node[1] not in [-1, self.m]:
                if not self.matrix[new_node[0]][new_node[1]] and self.arr[new_node[0]][new_node[1]] == 1:
                    self.matrix[new_node[0]][new_node[1]] = True
                    self.dfs(new_node)

    def solve_main(self):

        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    self.res += 1
                    self.dfs([i, j])
        print(self.res)


# bfs版本
class Solve1:

    def __init__(self, n=None, m=None, input_arr=None):
        self.direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 方向设置顺时针 上右下左（上下左右这么设置方向会有坑，就顺时针或者逆时针）
        self.res = 0
        if None not in [n, m, input_arr]:
            # 参数传递
            self.n, self.m = n, m
            self.arr = input_arr
            self.matrix = [[False] * self.m for _ in range(self.n)]  # 二维数组（用作记录是否遍历过当前元素）

        else:
            # acm input
            def get_line_input():
                return map(int, input().split())

            self.n, self.m = get_line_input()
            self.matrix = [[False] * self.m for _ in range(self.n)]
            self.arr = []
            for i in range(self.n):
                sgl_input = get_line_input()
                self.arr.append(list(sgl_input))

    def bfs(self, work_nodes):
        while len(work_nodes) > 0:
            cur_node = work_nodes.pop(0)
            for e in self.direct:
                next_node = [cur_node[0] + e[0], cur_node[1] + e[1]]
                if next_node[0] in [-1, self.n] or next_node[1] in [-1, self.m]:
                    continue
                if self.arr[next_node[0]][next_node[1]] == 1 and not self.matrix[next_node[0]][next_node[1]]:
                    work_nodes.append(next_node)
                    self.matrix[next_node[0]][next_node[1]] = True  # ！细节，在push进队列的时候标记，避免重复push

    def solve_main(self):

        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] and self.arr[i][j] == 1:
                    self.res += 1
                    self.bfs([[i, j]])
        print(self.res)


if __name__ == "__main__":
    # tst_obj = Solve(4, 5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
    # tst_obj.solve_main()

    tst_obj = Solve1(4, 5, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
    tst_obj.solve_main()
    ...
