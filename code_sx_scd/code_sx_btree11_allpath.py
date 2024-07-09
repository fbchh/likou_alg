"""
xxx
"""


# 递归法
def solve(root, targetSum):
    if not root:
        return False

    def inner_func(cur, cur_sum):
        if not cur.left and not cur.right:
            return False if cur_sum != 0 else True

        if cur.left:
            if inner_func(cur.left, cur_sum - cur.left.val):
                return True
        if cur.right:
            if inner_func(cur.right, cur_sum - cur.right.val):
                return True
        return False

    return inner_func(root, targetSum - root.val)


if __name__ == "__main__":
    pass
