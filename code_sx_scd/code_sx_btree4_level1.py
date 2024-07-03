"""
xxx
"""


# 广度优先——层序遍历——队列方式
def solve1(root):
    if not root:
        return []

    _list = [root]
    res = []
    while len(_list) > 0:
        sgl_level = []
        for _ in range(len(_list)):
            cur = _list.pop(0)
            sgl_level.append(cur.val)
            if cur.left:
                _list.append(cur.left)
            if cur.right:
                _list.append(cur.right)
        res.append(sgl_level)
    return res


# 广度优先——层序遍历——递归法
def solve2(root):
    if not root:
        return []

    res = []

    def inner_func(btree_node, level):
        if not btree_node:
            return None

        if len(res) == level:
            res.append([])

        res[level].append(btree_node.val)
        inner_func(btree_node.left, level + 1)
        inner_func(btree_node.right, level + 1)

    inner_func(root, 0)
    return res


if __name__ == "__main__":
    pass
