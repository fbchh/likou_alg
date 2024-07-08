"""
xxx
"""


# 层序遍历法
def solve(root):
    if not root:
        return None

    res = []
    _list = [root]
    while _list:
        sgl_elems = []
        for _ in range(len(_list)):
            cur = _list.pop(0)
            sgl_elems.append(cur.val)
            if cur.left:
                _list.append(cur.left)
            if cur.right:
                _list.append(cur.right)
        res.append(sgl_elems)
    return res[-1][0]


# 递归法
class Solution:
    max_len = 0
    res = 0

    def solve1(self, root):

        def inner_fun(cur, depth):
            if not cur.left and not cur.right:
                if depth > self.max_len:
                    self.max_len = depth
                    self.res = cur.val
                return

            if cur.left:
                inner_fun(cur.left, depth + 1)

            if cur.right:
                inner_fun(cur.right, depth + 1)

        inner_fun(root, 1)
        return self.res


if __name__ == "__main__":
    pass
