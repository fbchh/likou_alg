"""
xxx
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(nums):
    def inner_func(cur_nums):
        new_node = TreeNode()
        if len(cur_nums) == 1:
            new_node.val = cur_nums[-1]
            return new_node

        max_val = max(cur_nums)
        max_val_index = cur_nums.index(max_val)
        new_node.val = max_val
        if max_val_index > 0:
            new_node.left = inner_func(cur_nums[:max_val_index])

        if max_val_index < len(cur_nums) - 1:
            new_node.right = inner_func(cur_nums[max_val_index + 1:])
        return new_node

    return inner_func(nums)


if __name__ == "__main__":
    tst_nums1 = [3, 2, 1, 6, 0, 5]
    tst_ege_res = solve(tst_nums1)
    print('')
    pass
