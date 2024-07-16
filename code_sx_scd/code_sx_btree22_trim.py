"""
xxx
"""


def solve(root, low, high):
    def inner_func(cur, l_num, r_num):
        if cur is None:
            return None

        if cur.val < l_num:
            return inner_func(cur.right, l_num, r_num)

        if cur.val > r_num:
            return inner_func(cur.left, l_num, r_num)

        cur.left = inner_func(cur.left, l_num, r_num)
        cur.right = inner_func(cur.right, l_num, r_num)
        return cur

    return inner_func(root, low, high)


if __name__ == "__main__":
    pass
