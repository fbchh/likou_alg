"""
xxx
"""


# 对称二叉树-递归法
def solve1(root):
    if not root:
        return True

    def inner_func(l_node, r_node):
        if not l_node and r_node:
            return False
        elif l_node and not r_node:
            return False
        elif l_node is None and r_node is None:
            return True
        elif l_node.val != r_node.val:
            return False

        return inner_func(l_node.left, r_node.right) and inner_func(l_node.right, r_node.left)

    return inner_func(root.left, root.right)


# 对称二叉树-迭代法
def solve2(root):
    if not root:
        return True

    _list = [root.left, root.right]
    while len(_list) > 0:
        cur1 = _list.pop(0)
        cur2 = _list.pop(0)

        if not cur1 and not cur2:
            continue
        if not cur1 or not cur2 or cur1.val != cur2.val:
            return False

        _list.append(cur1.left)
        _list.append(cur2.right)
        _list.append(cur1.right)
        _list.append(cur2.left)

    return True


if __name__ == "__main__":
    pass
