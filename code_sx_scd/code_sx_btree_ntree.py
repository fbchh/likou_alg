"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children  # 可遍历的对象
"""


def solve1(root):
    if not root:
        return []

    _list = [root]
    res = []
    while len(_list) > 0:
        level_res = []
        for _ in range(len(_list)):
            cur = _list.pop(0)
            level_res.append(cur.val)

            for sub_node in cur.children:
                _list.append(sub_node)

        res.append(level_res)

    return res


if __name__ == "__main__":
    pass
