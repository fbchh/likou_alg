"""
xxx
"""


def solve(root, val):
    def inner_func(cur, tgt_num):
        if cur is None:
            return None

        if cur.val == tgt_num:  # 核心逻辑
            if cur.left is None and cur.right is None:
                return None
            elif cur.left is None and cur.right is not None:
                return cur.right
            elif cur.left is not None and cur.right is None:
                return cur.left
            elif cur.left is not None and cur.right is not None:
                sp = cur.right
                sp_last = None
                while sp is not None:
                    sp_last = sp
                    sp = sp.left
                sp_last.left = cur.left
                return cur.right

        if tgt_num < cur.val:
            cur.left = inner_func(cur.left, tgt_num)
        elif tgt_num > cur.val:
            cur.right = inner_func(cur.right, tgt_num)
        return cur

    return inner_func(root, val)


if __name__ == "__main__":
    pass
