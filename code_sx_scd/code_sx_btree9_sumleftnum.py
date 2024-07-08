"""
xxx
"""


def solve(root):
    def inner_func(cur_node):
        if not cur_node:
            return 0
        if not cur_node.left and not cur_node.right:
            return 0

        left_num = inner_func(cur_node.left)
        if cur_node.left and not cur_node.left.left and not cur_node.left.right:
            left_num = cur_node.left.val

        right_num = inner_func(cur_node.right)
        return left_num + right_num

    return inner_func(root)


if __name__ == "__main__":
    pass
