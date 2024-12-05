"""
xxx
"""


class Solve:
    def __init__(self):
        def sgl_line_input():
            return map(int, input().strip().split())

        self.inner_max = float("inf")
        self.n, self.m = sgl_line_input()
        self.graph = [[self.inner_max] * (self.n + 1) for _ in range(self.n + 1)]
        self.is_used = [False] * (self.n + 1)
        self.min_dist = [self.inner_max] * (self.n + 1)
        self.min_dist[1] = 0

        for _ in range(self.m):
            idx1, idx2, val = sgl_line_input()
            self.graph[idx1][idx2] = val

    def solve_main(self):
        for _ in range(1, self.n + 1):
            # find、choose
            last_node_idx = -1
            last_min_dist = self.inner_max

            for j in range(1, self.n + 1):
                if not self.is_used[j] and self.min_dist[j] < last_min_dist:
                    last_min_dist = self.min_dist[j]
                    last_node_idx = j

            if last_node_idx == -1:
                break

            self.is_used[last_node_idx] = True

            # update
            for j in range(1, self.n + 1):
                if (not self.is_used[j] and self.graph[last_node_idx][j] != self.inner_max and
                        self.min_dist[j] > self.graph[last_node_idx][j] + self.min_dist[last_node_idx]):
                    self.min_dist[j] = self.min_dist[last_node_idx] + self.graph[last_node_idx][j]

        res = self.min_dist[self.n]
        res = -1 if res == self.inner_max else res
        print(res)
        return res


if __name__ == "__main__":
    tst_obj = Solve()
    tst_obj.solve_main()
    ...
