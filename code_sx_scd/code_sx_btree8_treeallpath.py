"""
xxx
"""


# 二叉树的所有路径——递归法
def solve(root):
    if not root:
        return None

    res = []
    deal_str = ''

    def inner_func(cur_node, s, arr_str):
        s += str(cur_node.val)
        if not cur_node.left and not cur_node.right:
            arr_str.append(s)

        if cur_node.left:
            inner_func(cur_node.left, s + "->", res)
        if cur_node.right:
            inner_func(cur_node.right, s + "->", res)

    inner_func(root, deal_str, res)
    return res


if __name__ == "__main__":
    pass
