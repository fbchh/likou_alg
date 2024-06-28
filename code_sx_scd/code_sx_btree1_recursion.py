"""
xxx
"""


class Btree:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


# 前序-中间节点在前（中->左->右）
def solve1(root):
    res = []

    def inner_func(node):
        if not node:
            return None

        res.append(node.val)
        inner_func(node.left)
        inner_func(node.right)

    inner_func(root)
    return res


# 中序
def solve2(root):
    res = []

    def inner_func(node):
        if not node:
            return None

        inner_func(node.left)
        res.append(node.val)
        inner_func(node.right)

    inner_func(root)
    return res


# 后序
def solve3(root):
    res = []

    def inner_func(node):
        if not node:
            return None

        inner_func(node.left)
        inner_func(node.right)
        res.append(node.val)

    inner_func(root)
    return res


if __name__ == "__main__":
    pass
