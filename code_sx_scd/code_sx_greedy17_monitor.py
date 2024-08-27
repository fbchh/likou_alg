"""
这题主要是分析过程会难到，代码跟简单
"""


class Solve:
    def __init__(self):
        self.camera_nums = 0

    def inner_func(self, bt_rt):
        """
        0-节点未覆盖
        1-节点被覆盖
        2-节点有像头
        """
        if bt_rt is None:
            return 1

        # 后续遍历
        l = self.inner_func(bt_rt.left)
        r = self.inner_func(bt_rt.right)

        # 叶子节点都被覆盖(整个树的叶子节点)
        if l == r == 1:
            return 0

        # 叶子结点至少有一个未覆盖
        if l == 0 or r == 0:
            self.camera_nums += 1
            return 2

        # 叶子节点至少有一个有像头
        if l == 1 or r == 1:
            return 1

    def minCameraCover(self, root):
        if self.inner_func(root) == 0:
            self.camera_nums += 1

        return self.camera_nums


if __name__ == "__main__":
    # leetcode 运行
    ...
