"""
xxx
"""


# 递归
def solve1(root, val):
    def inner_func(node, tgt_num):
        if not node.left and not node.right and node.val != tgt_num:
            return None

        if node.val == tgt_num:
            return node
        if node.left:
            l_res = inner_func(node.left, tgt_num)
            if l_res:
                return l_res

        if node.right:
            r_res = inner_func(node.right, tgt_num)
            if r_res:
                return r_res

    return inner_func(root, val)


# 迭代
def solve2(root, val):
    _list = [root]
    while len(_list) > 0:
        cur_node = _list.pop(0)
        if cur_node.val == val:
            return cur_node
        if cur_node.left:
            _list.append(cur_node.left)

        if cur_node.right:
            _list.append(cur_node.right)

    return None


if __name__ == "__main__":
    pass
