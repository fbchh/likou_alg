"""
二叉树16、17、18、19总结

    找树左下角的值
        递归、迭代均可，更倾向于迭代的层序遍历 二叉树截止到现在有两种层序遍历一种是每层元素最后添加None节点标记、另一种在单次迭代中获取当前层元素个数
    路径总和
        建议使用递归，更方便做回溯 使用迭代法需要考虑使用自定义数据结构同时记录节点指针和根节点到当前节点的和
    中/后序构造二叉树
        本题重点是结合后续数组与中序数组做切割  就这种情况应该只能使用递归
    最大二叉树
        采用递归的手法实现，但是需要注意在处理左右子节点的时候注意判断区间元素是否存在
"""


def solve():
    ...


if __name__ == "__main__":
    ...
