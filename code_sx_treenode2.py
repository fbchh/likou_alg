"""
代码随想录学习记录
章节：二叉树
题目：二叉树的递归遍历

    题意：
    练习二叉树的前、中、后序遍历

    什么顺序取决于中间节点的遍历顺序，如下：（帮助理解记忆）
        前序遍历：中左右
        中序遍历：左中右
        后序遍历：左右中
"""


class TreeNode(object):

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve1(tree_node):
    """
    前序遍历
    :param tree_node: xx
    :return: xx
    """
    _res = []

    def dfs(tree):

        if tree is None:
            return
        _res.append(tree.val)
        dfs(tree.left)
        dfs(tree.right)

    dfs(tree_node)
    return _res


def solve2(tree_node):
    """
    中序遍历
    :param tree_node: xx
    :return: xx
    """
    _res = []

    def dfs(b_tree):
        if b_tree is None:
            return
        dfs(b_tree.left)
        _res.append(b_tree.val)
        dfs(b_tree.right)

    dfs(tree_node)
    return _res


def solve3(tree_node):
    """
    后序遍历
    :param tree_node: xx
    :return: xx
    """
    _res = []

    def dfs(b_tree):
        if b_tree is None:
            return
        dfs(b_tree.left)
        dfs(b_tree.right)
        _res.append(b_tree.val)

    dfs(tree_node)
    return _res


if __name__ == "__main__":
    # def build_tst_data(nums):
    #
    #     for i in range(0, len(nums), 2):
    #         _l_val = nums[i+1] if i+1 < len(nums) else None
    #         _r_val = nums[i+1] if i+2 < len(nums) else None
    #         _l = TreeNode(val=_l_val)
    #         _r = TreeNode(val=_r_val)
    #         _mid = TreeNode(val=nums[i], l_next=_l, r_next=_r)
    #
    #         pass
    #     pass

    # 本地构建二叉树的输入数据有点困难，直接在力扣上测试的，在随想录官方对应的章节中有传送门
    pass
