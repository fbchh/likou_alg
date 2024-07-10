"""
xxx
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归实现如下
def solve(root1, root2):
    def inner_func(cur_root1, cur_root2):
        if not cur_root1:
            return cur_root2
        if not cur_root2:
            return cur_root1

        new_node = TreeNode(cur_root1.val + cur_root2.val)
        new_node.left = inner_func(cur_root1.left, cur_root2.left)
        new_node.right = inner_func(cur_root1.right, cur_root2.right)

        return new_node

    return inner_func(root1, root2)


# 层序遍历的思想
def solve1(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1

    _list = [root1, root2]
    while len(_list) > 0:
        node1 = _list.pop(0)
        node2 = _list.pop(0)
        node1.val += node2.val
        if node1.left and node2.left:
            _list.append(node1.left)
            _list.append(node2.left)

        if node1.right and node2.right:
            _list.append(node1.right)
            _list.append(node2.right)

        if not node1.left and node2.left:
            node1.left = node2.left

        if not node1.right and node2.right:
            node1.right = node2.right

    return root1


if __name__ == "__main__":
    pass
