"""
代码随想录学习记录
章节：二叉树
题目：二叉树的统一迭代法

    题意：
    基于栈的迭代法思想的二叉树的三种遍历方式在是实现上代码不统一。不像递归遍历，代码比较统一，只需稍做修改即可。
"""


def solve1(tree_node):
    """
    统一迭代——前序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []
    work_stack = [tree_node]
    res = []
    while work_stack:
        cur_node = work_stack.pop()
        if cur_node:
            if cur_node.right:  # 右
                work_stack.append(cur_node.right)

            if cur_node.left:  # 左
                work_stack.append(cur_node.left)

            work_stack.append(cur_node)  # 中
            work_stack.append(None)
        else:
            cur_node = work_stack.pop()
            res.append(cur_node.val)
    return res


def solve2(tree_node):
    """
    统一迭代——中序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []
    work_stack = [tree_node]
    res = []
    while work_stack:
        cur_node = work_stack.pop()
        if cur_node:
            if cur_node.right:  # 右
                work_stack.append(cur_node.right)

            work_stack.append(cur_node)  # 中
            work_stack.append(None)

            if cur_node.left:  # 左
                work_stack.append(cur_node.left)
        else:
            cur_node = work_stack.pop()
            res.append(cur_node.val)
    return res


def solve3(tree_node):
    """
    统一迭代——后序遍历
    :param tree_node: xx
    :return: xx
    """
    if not tree_node:
        return []
    work_stack = [tree_node]
    res = []
    while work_stack:
        cur_node = work_stack.pop()
        if cur_node:
            work_stack.append(cur_node)  # 中
            work_stack.append(None)

            if cur_node.right:  # 右
                work_stack.append(cur_node.right)

            if cur_node.left:  # 左
                work_stack.append(cur_node.left)
        else:
            cur_node = work_stack.pop()
            res.append(cur_node.val)
    return res


if __name__ == "__main__":
    pass
