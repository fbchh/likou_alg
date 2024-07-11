"""
xxx
"""


# 递归1
class Solution():
    def __init__(self):
        self.max_val = float('-inf')

    def solve1(self, root):
        def inner_func(cur):
            if not cur:
                return True

            bool_l = inner_func(cur.left)
            if self.max_val < cur.val:
                self.max_val = cur.val
            else:
                return False
            bool_r = inner_func(cur.right)

            return bool_l & bool_r

        return inner_func(root)


# 迭代
def solve2(root):
    _stack = [root]

    pre = None
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
            if pre is None:
                pre = cur.val
            else:
                if cur.val <= pre:
                    return False
                pre = cur.val
    return True


if __name__ == "__main__":
    pass
