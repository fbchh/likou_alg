"""
代码随想录学习记录
章节：链表
题目：移除链表元素

    题意：删除链表中等于给定值 val 的所有节点。

    示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]

    示例 2： 输入：head = [], val = 1 输出：[]

    示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
"""
import json


# 链表的定义
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def init_list_node(input_arr):
    """
    将输入的数据初始化为单向链表
    :param input_arr: xx
    :return: xx
    """
    _v_head_node = ListNode(None)
    current_node = _v_head_node
    for e in input_arr:
        current_node.next = ListNode(e)
        current_node = current_node.next
    return _v_head_node.next


def list_node2arr(input_list_node):
    """
    将输入的单向链表取出数值，并格式化为数组
    :param input_list_node: xx
    :return: xx
    """
    if input_list_node is not None:
        _res = []
        cur_node = input_list_node
        while True:
            _res.append(cur_node.val)
            if not cur_node.next:
                break
            cur_node = cur_node.next
        return _res
    else:
        return []


def solve1(input_list_node, input_num):
    """
    创建虚拟头节点，使得移除头节点和移除其他节点的操作一致
    移除指定val节点操作的实现：获取下一个节点的val,如果能和目标值匹配，
    把当前节点的next替换为下一个节点的next，这样，中间节点就从整个链表中删除
    :param input_list_node: xx
    :param input_num: xx
    :return: xx
    """
    if input_list_node is not None:
        _inner_node = ListNode(None, input_list_node)
        current_node = _inner_node
        while current_node.next:
            if current_node.next.val == input_num:
                current_node.next = current_node.next.next
            else:
                # 这里在第一次写的时候存在的问题：两种情况均将当前节点向后移动，
                # 正确的思想应该是确认当前节点不符合条件时，才将当前节点更新到下一个节点
                current_node = current_node.next
        return _inner_node.next


def fun_tst(input_arr, input_val):
    """
    用例测试
    :param input_arr: xx
    :param input_val: xx
    :return:xx
    """
    input_node1 = init_list_node(input_arr)
    deal_node = solve1(input_node1, input_val)
    res = list_node2arr(deal_node)
    print(res)
    return res


if __name__ == "__main__":
    from time import time

    t1 = time()

    # # 初始化链表示例
    # a = ListNode(5)
    # b = ListNode(6)
    # a.next = b
    # print(f"[run info] listNode: {a.next.val}")

    # # 自定义格式化和反格式化的方法示例
    # tst_arr = [1, 2, 3, 4]
    # tst_node = init_list_node(tst_arr)
    # tst_arr1 = list_node2arr(tst_node)
    # print(tst_arr1 == tst_arr)

    tst_arr1 = [1, 2, 6, 3, 4, 5, 6]
    val1 = 6
    fun_tst(tst_arr1, val1)

    fun_tst([], 1)
    fun_tst([7, 7, 7, 7], 7)

    t2 = time()
    print(f"[info] tol cost sec: {t2 - t1}S")
