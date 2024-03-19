"""
代码随想录学习记录
章节：链表
题目：删除链表的倒数第N个节点

    题意：

    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    进阶：你能尝试使用一趟扫描实现吗？
    示例 1：
    输入：head = [1,2,3,4,5], n = 2 输出：[1,2,3,5]
    示例 2：
    输入：head = [1], n = 1 输出：[]
    示例 3：
    输入：head = [1,2], n = 1 输出：[1]
"""
from time import time


def count_time(input_func):
    t1 = time()
    input_func()
    print(f"[info] tol cost sec: {time() - t1}S")


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def arr2node(input_arr):
    v_head_node = ListNode()
    cur_node = v_head_node
    for e in input_arr:
        cur_node.next = ListNode(e)
        cur_node = cur_node.next
    return v_head_node.next


def solve1(input_node, reverse_index):
    """
    解法1，两次遍历，一次获取链表长度，一次删除
    :param input_node:xx
    :param reverse_index:xx
    :return:xx
    """
    _len = 0
    cur_node = input_node
    while cur_node:
        _len += 1
        cur_node = cur_node.next

    tar_index = _len - reverse_index
    v_node = ListNode(next=input_node)
    cur_node = v_node
    _index = -1
    l_node = v_node
    while cur_node:
        if _index == tar_index:
            l_node.next = cur_node.next
            break
        _index += 1
        l_node = cur_node
        cur_node = cur_node.next
    return v_node.next


def solve2(input_node, reverse_index):
    """
    解法2，基于双指针，核心思想是快慢指针的间隔为reverse，
    这样，在快指针到达末尾的时候，慢指针的值刚好就可以删除
    (原先的想法<以上>有问题，下面的代码为随想录的推荐写法)
    :param input_node:xx
    :param reverse_index:xx
    :return:xx
    """
    v_head_node = ListNode(next=input_node)
    r_node = l_node = v_head_node

    # 快指针先“跑”，领先慢指针+1个后，等到快指针到链表结尾的时候，慢指针的下一个即为需要删除的节点
    for _ in range(reverse_index + 1):
        r_node = r_node.next

    while r_node:
        r_node = r_node.next
        l_node = l_node.next

    l_node.next = l_node.next.next
    return v_head_node.next


if __name__ == "__main__":
    # list_node1 = arr2node(list(range(1, 6)))
    # res_node1 = solve1(list_node1, 2)
    #
    # list_node2 = arr2node(list(range(1, 2)))
    # res_node2 = solve1(list_node2, 1)

    # list_node3 = arr2node(list(range(1, 3)))
    # res_node3 = solve1(list_node3, 1)

    list_node1 = arr2node(list(range(1, 3)))
    res1 = solve2(list_node1, 1)

    def tst1():
        solve1(arr2node(list(range(10000000))), 99)

    def tst2():
        solve2(arr2node(list(range(10000000))), 99)

    count_time(tst1)
    count_time(tst2)
    """
    时间对比：
        [info] tol cost sec: 7.256872653961182S
        [info] tol cost sec: 6.267966270446777S
    """
    # print()
