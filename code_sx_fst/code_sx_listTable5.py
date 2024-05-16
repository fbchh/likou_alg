"""
代码随想录学习记录
章节：链表
题目：两两交换链表中的节点

    题意：

    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
"""
from time import time


class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def init_list_node_by_arr(input_arr):
    v_head_node = ListNode()
    cur_node = v_head_node
    for e in input_arr:
        cur_node.next = ListNode(e)
        cur_node = cur_node.next
    return v_head_node.next


def solve1(input_list_node):
    """
    解法1,使用一个满二处理的条件，处理后变量置1
    :param input_list_node:
    :return:
    """
    _count = 1
    l_node = None
    r_node = input_list_node
    while r_node:
        if _count == 2:
            _val = l_node.val
            l_node.val = r_node.val
            r_node.val = _val
            _count = 1
        elif _count == 1:
            _count += 1
        l_node = r_node
        r_node = r_node.next

    return input_list_node


if __name__ == "__main__":
    list_node1 = init_list_node_by_arr([1, 2, 3, 4])
    list_node2 = solve1(list_node1)

    list_node3 = init_list_node_by_arr(list(range(1,100)))
    list_node4 = solve1(list_node3)
    print(111)
