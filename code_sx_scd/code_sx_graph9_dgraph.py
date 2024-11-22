"""
xxx
"""
from collections import deque, defaultdict


class Solve:
    def __init__(self, n=None, m=None, graph=None):
        if None in [n, m, graph]:
            def sgl_line_input():
                return map(int, input().split())

            self.graph = defaultdict(deque)
            self.n, self.m = sgl_line_input()
            for _ in range(self.m):
                sgl_line_num1, sgl_line_num2 = sgl_line_input()
                self.graph[sgl_line_num1].append(sgl_line_num2)
        else:
            self.n, self.m = n, m
            self.graph = graph
        self.res_nodes = set()

    def dfs(self, work_node):
        self.res_nodes.add(work_node)
        while len(self.graph[work_node]) > 0:
            self.dfs(self.graph[work_node].popleft())

    def bfs(self, work_que):
        while len(work_que) > 0:
            cur_node = work_que.popleft()
            self.res_nodes.add(cur_node)
            for e in self.graph[cur_node]:
                work_que.append(e)
            self.graph[cur_node] = deque()

    def solve_main(self, mode=2):
        """
        mode 1--dfs 2--bfs
        """
        if mode == 2:
            self.bfs(deque([1]))
        elif mode == 1:
            self.dfs(1)

        if self.res_nodes == {i for i in range(1, self.n + 1)}:
            print(1)
        else:
            print(-1)


if __name__ == "__main__":
    tst_obj = Solve(4, 4, {
        1: deque([2, 3]),
        2: deque([1, 4]),
        3: deque(),
        4: deque()
    })
    tst_obj.solve_main(1)
    ...
