"""
xxx
"""


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
    res.reverse()
    return res


if __name__ == "__main__":
    pass
