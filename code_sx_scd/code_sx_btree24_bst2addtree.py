"""
xxx
"""


# 递归顺序——右、中、左
class Solve:
    def __init__(self):
        self.pre_num = 0

    def solve(self, root):
        def inner_func(cur):
            if cur is None:
                return
            inner_func(cur.right)
            cur.val += self.pre_num
            self.pre_num = cur.val
            inner_func(cur.left)

        inner_func(root)
        return root


if __name__ == "__main__":
    pass
