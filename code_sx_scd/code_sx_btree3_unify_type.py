"""
xxx
"""


# 统一写法 前序
def solve1(root):
    if not root:
        return []
    _stack = [root]
    res = []
    while len(_stack) > 0:
        cur = _stack.pop()
        if cur:
            if cur.right:
                _stack.append(cur.right)
            if cur.left:
                _stack.append(cur.left)
            _stack.append(cur)
            _stack.append(None)
        else:
            cur = _stack.pop()
            res.append(cur.val)
    return res


# 统一写法 中序
def solve2(root):
    if not root:
        return []
    _stack = [root]
    res = []
    while len(_stack) > 0:
        cur = _stack.pop()
        if cur:
            if cur.right:
                _stack.append(cur.right)
            _stack.append(cur)
            _stack.append(None)
            if cur.left:
                _stack.append(cur.left)
        else:
            cur = _stack.pop()
            res.append(cur.val)
    return res


# 统一写法 后序
def solve3(root):
    if not root:
        return []
    _stack = [root]
    res = []
    while len(_stack) > 0:
        cur = _stack.pop()
        if cur:
            _stack.append(cur)
            _stack.append(None)
            if cur.right:
                _stack.append(cur.right)
            if cur.left:
                _stack.append(cur.left)
        else:
            cur = _stack.pop()
            res.append(cur.val)
    return res


if __name__ == "__main__":
    pass
