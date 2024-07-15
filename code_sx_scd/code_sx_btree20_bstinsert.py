"""
xxx
"""


class TreeNode:
    def __init__(self, val=None, l=None, r=None):
        self.left = l
        self.right = r
        self.val = val


# 递归写法
def solve(root, val):
    def inner_func(cur, tgt_num):
        if cur is None:
            return TreeNode(tgt_num)

        if cur.val > tgt_num:
            cur.left = inner_func(cur.left, tgt_num)
        elif cur.val < tgt_num:
            cur.right = inner_func(cur.right, tgt_num)

        return cur

    return inner_func(root, val)


# 迭代写法-重点是找到需要插入的节点的位置
def solve1(root, val):
    if root is None:
        return TreeNode(val)

    cur = root
    last_node = None
    while cur is not None:
        last_node = cur
        if cur.val > val:
            cur = cur.left
        elif cur.val < val:
            cur = cur.right

    new_node = TreeNode(val)
    if val < last_node.val:
        last_node.left = new_node
    elif val > last_node.val:
        last_node.right = new_node

    return root


if __name__ == "__main__":
    pass
