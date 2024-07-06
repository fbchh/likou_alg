"""
xxx
"""


# 判断二叉树是否为平衡二叉树——递归法
def solve(root):
    def inner_func(cur_node):
        if not cur_node:
            return 0

        l_node_h = inner_func(cur_node.left)
        if l_node_h == -1:
            return -1

        r_node_h = inner_func(cur_node.right)
        if r_node_h == -1:
            return -1
        return -1 if abs(l_node_h - r_node_h) > 1 else max(l_node_h, r_node_h) + 1

    return inner_func(root) != -1


if __name__ == "__main__":
    pass
