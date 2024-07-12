"""
xxx
"""


# 递归-未优化（中序+循环）
def solve(root):
    tree_vals = []

    def inner_func(cur):
        if not cur:
            return
        inner_func(cur.left)
        tree_vals.append(cur.val)
        inner_func(cur.right)

    inner_func(root)
    min_res = float('inf')
    for i in range(1, len(tree_vals)):
        _ = abs(tree_vals[i] - tree_vals[i - 1])
        if _ < min_res:
            min_res = _
    return min_res


# 递归-优化后（中序）
class Solve:
    def __init__(self):
        self.min_val = float('inf')
        self.pre_num = None

    def solve(self, cur):
        if not cur:
            return

        self.solve(cur.left)
        if self.pre_num:
            self.min_val = min(self.min_val, cur.val - self.pre_num)
        self.pre_num = cur.val
        self.solve(cur.right)

    def getMinimumDifference(self, root):
        self.solve(root)
        return self.min_val


# 迭代法
def solve2(root):
    _stack = []
    cur = root
    pre = None
    min_val = float('inf')
    while cur or len(_stack) > 0:
        if cur:
            _stack.append(cur)
            cur = cur.left
        else:
            cur = _stack.pop()
            if pre is not None:
                min_val = min(min_val, cur.val - pre)
            pre = cur.val
            cur = cur.right

    return min_val


if __name__ == "__main__":
    pass
