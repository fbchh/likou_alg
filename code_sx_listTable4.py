"""
代码随想录学习记录
章节：链表
题目：翻转链表

    题意：反转一个单链表。

    示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
"""
from time import time


def count_time(input_process, *input_params1, **input_params2):
    if callable(input_process):
        t1 = time()
        res = input_process(*input_params1, **input_params2)
        print(f"tol cost sec: {time() - t1}S")
        return res
    else:
        print("[error] input process must be callable")


class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def init_list_node(input_arr):
    """
    将输入的数据初始化为单向链表
    :param input_arr: xx
    :return: xx
    """
    _v_head_node = ListNode()
    current_node = _v_head_node
    for e in input_arr:
        current_node.next = ListNode(e)
        current_node = current_node.next
    return _v_head_node.next


def solve1(input_list_node):
    """
    解法1，先顺序遍历出所有的节点值，然后再初始化另外一个链表
    :param input_list_node:xx
    :return:xx
    """
    cur_node = input_list_node
    _res = []
    while 1:
        _res.append(cur_node.val)
        if cur_node.next is None:
            break
        cur_node = cur_node.next
    _res.reverse()
    _res_node = init_list_node(_res)
    return _res_node


def solve2(input_list_node):
    """
    解法2，双指针法，直接在原先的链表基础上修改其next指向
    :param input_list_node:
    :return:
    """
    cur_node = input_list_node
    last_node = None
    while 1:
        after_node = cur_node.next
        cur_node.next = last_node

        if after_node is None:  # 边界条件一定要考虑清楚，这里边界条件没有考虑清楚，浪费很长时间
            return cur_node
        last_node = cur_node
        cur_node = after_node


if __name__ == "__main__":

    def tst1():
        list_node1 = init_list_node(list(range(100000)))
        list_node2 = solve1(list_node1)

    def tst2():
        list_node1 = init_list_node(list(range(100000)))
        list_node2 = solve2(list_node1)

    count_time(tst1)
    count_time(tst2)

    """
    时间对比：
        tol cost sec: 0.0989992618560791S
        tol cost sec: 0.042000532150268555S
        
    时间分析，slove1相对于solve2多了一次对链表的创建，对同样长度链表的访问次数为2，所以时间上就体现出2倍的差异
    """