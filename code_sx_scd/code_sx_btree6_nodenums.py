"""
xxx
"""


# 完全二叉树节点个数——递归法
def solve(root):
    if not root:
        return 0

    def inner_func(cur_node):
        if not cur_node:
            return 0
        return 1 + inner_func(cur_node.left) + inner_func(cur_node.right)

    return inner_func(root)


if __name__ == "__main__":
    pass
