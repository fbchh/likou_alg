"""
xxx
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(nums):
    def inner_func(arr, l_idx, r_idx):
        if l_idx > r_idx:
            return None

        mid_idx = l_idx + (r_idx - l_idx) // 2
        new_root = TreeNode(arr[mid_idx])
        new_root.left = inner_func(arr, l_idx, mid_idx - 1)
        new_root.right = inner_func(arr, mid_idx + 1, r_idx)
        return new_root

    return inner_func(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    pass
