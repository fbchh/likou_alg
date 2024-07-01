"""
xxx
"""


# 前序 迭代法遍历
def solve1(root):
    if not root:
        return []

    _stack = [root]
    res = []
    while len(_stack) > 0:
        cur = _stack.pop()
        res.append(cur.val)

        if cur.right:
            _stack.append(cur.right)
        if cur.left:
            _stack.append(cur.left)

    return res


# 中序
def solve2(root):
    _stack, cur, res = [], root, []
    while cur or len(_stack) > 0:
        if cur:
            _stack.append(cur)
            cur = cur.left  # 中->左
        else:
            cur = _stack.pop()
            res.append(cur.val)
            cur = cur.right()  # 当前节点为空，返回上一层的节点的右节点

    return res


# 后序
def solve3(root):
    if not root:
        return []
    _stack, res = [root], []
    while _stack:
        cur = _stack.pop()
        res.append(cur.val)
        if cur.left:
            _stack.append(cur.left)
        if cur.right:
            _stack.append(cur.right)
    res.reverse()
    return res


if __name__ == "__main__":
    pass
