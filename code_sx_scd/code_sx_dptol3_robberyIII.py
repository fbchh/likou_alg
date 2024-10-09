"""
xxx
"""


def solve(root):
    def inner_func(tgt_root):
        if tgt_root is None:
            return [0, 0]

        left_num = inner_func(tgt_root.left)
        right_num = inner_func(tgt_root.right)

        num1 = max(left_num) + max(right_num)
        num2 = tgt_root.val + left_num[0] + right_num[0]
        # no cur; yes cur
        return [num1, num2]

    return max(inner_func(root))


if __name__ == "__main__":
    """
        leetcode 官网测试
    """
    ...
