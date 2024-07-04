"""
xxx
"""


# 递归法翻转二叉树
def solve1(root):
    if not root:
        return None

    def inner_func(cur_node):
        if not cur_node:
            return

        _ = cur_node.left
        cur_node.left = cur_node.right
        cur_node.right = _

        inner_func(cur_node.left)
        inner_func(cur_node.right)

    inner_func(root)
    return root


if __name__ == "__main__":
    pass
