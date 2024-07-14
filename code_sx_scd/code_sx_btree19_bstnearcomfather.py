"""
xxx
"""


def solve(root, p, q):
    if p.val > q.val:
        _ = q
        q = p
        p = _

    def inner_func(cur, node1, node2):
        if cur is None:
            return None

        if cur.val < node1.val:
            l_res = inner_func(cur.right, node1, node2)
            if l_res is not None:
                return l_res

        if cur.val > node2.val:
            r_res = inner_func(cur.left, node1, node2)
            if r_res is not None:
                return r_res

        return cur

    return inner_func(root, p, q)


if __name__ == "__main__":
    pass
