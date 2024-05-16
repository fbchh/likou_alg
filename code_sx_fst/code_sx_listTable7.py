"""
代码随想录学习记录
章节：链表
题目：链表相交

    题意：

    给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
    题目数据 保证 整个链式结构中不存在环。
    注意，函数返回结果后，链表必须 保持其原始结构
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def arr2node(input_arr):
    v_head = ListNode()
    cur_node = v_head
    for e in input_arr:
        cur_node.next = ListNode(e)
        cur_node = cur_node.next
    return v_head.next


def solve1(input_node1, input_node2):
    """
    解法1，先遍历各自长度，然后对齐检查的起始点，长的“先跑”，这段链表本身也不可能存在交点
    :param input_node1: xx
    :param input_node2: xx
    :return: xx
    """
    v_head_node1 = ListNode(next=input_node1)
    v_head_node2 = ListNode(next=input_node2)

    cur_node1 = v_head_node1
    _len1 = 0
    while cur_node1:
        _len1 += 1
        cur_node1 = cur_node1.next

    cur_node2 = v_head_node2
    _len2 = 0
    while cur_node2:
        _len2 += 1
        cur_node2 = cur_node2.next

    cur_node1 = v_head_node1
    cur_node2 = v_head_node2
    run_node, after_node = (cur_node1, cur_node2) if _len1 >= _len2 else (cur_node2, cur_node1)
    for _ in range(abs(_len1 - _len2)):
        run_node = run_node.next

    while run_node and after_node:
        # if run_node.val == after_node.val:  # 在本地不好给测试用例 用val值判断逻辑代替
        if run_node.next == after_node.next:
            return run_node.next  # 记得这里的返回值只有一个，看题目以为是两个。。。
        run_node = run_node.next
        after_node = after_node.next

    return None


if __name__ == "__main__":
    list_node1 = solve1(arr2node(list(range(5, 10))), arr2node(list(range(3, 10))))
    print(list_node1)
