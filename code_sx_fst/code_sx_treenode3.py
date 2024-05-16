"""
代码随想录学习记录
章节：二叉树
题目：二叉树的迭代遍历

    题意：
    二叉树的迭代遍历（*）
"""


def solve1(tree_node):
    """
    迭代法——二叉树的前序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []
    _work_stack = [tree_node]
    _res = []
    while _work_stack:

        cur_node = _work_stack.pop()
        _res.append(cur_node.val)

        if cur_node.right:  # “右”先入栈，后操作
            _work_stack.append(cur_node.right)

        if cur_node.left:  # “左”后入栈，先操作
            _work_stack.append(cur_node.left)
    return _res


def solve2(tree_node):
    """
    迭代法——中序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []

    _work_stack = []  # 不在初始化的时候放tree_node的考量出于在迭代的处理逻辑（如果对这里的理解忘记了，可以把tree_node带进去试一下）
    _res = []
    cur = tree_node
    while _work_stack or cur:
        if cur:
            _work_stack.append(cur)
            cur = cur.left
        else:
            cur = _work_stack.pop()
            _res.append(cur.val)
            cur = cur.right
    return _res


def solve3(tree_node):
    """
    迭代法——二叉树后序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []

    _work_stack = [tree_node]
    _res = []
    while _work_stack:

        cur_node = _work_stack.pop()
        _res.append(cur_node.val)

        if cur_node.left:
            _work_stack.append(cur_node.left)

        if cur_node.right:
            _work_stack.append(cur_node.right)

    return _res[::-1]  # 遍历结果（“中右左”）翻转即可得到“左右中”


if __name__ == "__main__":
    pass
