"""
xxx
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def solve(mid_arr, last_arr):
    def inner_func(cur_mid, cur_last):
        if len(cur_last) == 0:
            return None

        root_val = cur_last[-1]
        root_node = TreeNode(root_val)
        if len(cur_last) == 1:
            return root_node

        in_mid_indx = cur_mid.index(root_val)
        next_mid_l, next_mid_r = cur_mid[0:in_mid_indx], cur_mid[in_mid_indx + 1:]
        len_l, len_r = len(next_mid_l), len(next_mid_r)
        next_last_l, next_last_r = cur_last[0:len_l], cur_last[len_l:-1]

        root_node.left = inner_func(next_mid_l, next_last_l)
        root_node.right = inner_func(next_mid_r, next_last_r)

        return root_node

    return inner_func(mid_arr, last_arr)


# 上面代码的优化版本，优化点：每次迭代不在需要新建数组，浪费时间、空间
def solve1(inorder, postorder):
    def inner_func(mid_arr, cur_mid_s, cur_mid_e, last_arr, cur_last_s, cur_last_e):
        if cur_last_e - cur_last_s == 0:
            return None

        cur_root_val = last_arr[cur_last_e - 1]
        cur_node = TreeNode(cur_root_val)
        if cur_last_e - cur_last_s == 1:
            return cur_node

        mid_index = -1
        for i in range(cur_mid_s, cur_mid_e):
            if mid_arr[i] == cur_root_val:
                mid_index = i
                break
        next_mid_l_range, next_mid_r_range = (cur_mid_s, mid_index), (mid_index + 1, cur_mid_e)
        _len_l = next_mid_l_range[1] - next_mid_l_range[0]
        next_last_l_range, next_last_r_range = (cur_last_s, cur_last_s + _len_l), (cur_last_s + _len_l, cur_last_e - 1)

        cur_node.left = inner_func(mid_arr, next_mid_l_range[0], next_mid_l_range[1], last_arr,
                                   next_last_l_range[0], next_last_l_range[1])
        cur_node.right = inner_func(mid_arr, next_mid_r_range[0], next_mid_r_range[1], last_arr,
                                    next_last_r_range[0], next_last_r_range[1])

        return cur_node

    return inner_func(inorder, 0, len(inorder), postorder, 0, len(postorder))


if __name__ == "__main__":
    pass
