"""
代码随想录学习记录
章节：链表
题目：环形链表

    题意：

    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    说明：不允许修改给定的链表。
"""


def solve1(input_node):
    """
    解法1，使用列表保存当前节点，如果在循环中发现“当前节点”在列表中已经存在则返回“当前节点”
    :param input_node:xx
    :return:xx
    """
    _history = set()
    cur_node = input_node
    while cur_node:
        if cur_node in _history:
            return cur_node
        _history.add(cur_node)
        cur_node = cur_node.next
    return None


def solve2(input_node):
    """
    解法2，使用快慢指针，快指针先移动n步，如果在循环中两个指针相同，快节点从当前向后，满节点从head向后，相遇的地方即为环的入口(随想录官方推荐写法)
    :param input_node:xx
    :return:xx
    """
    l_node = r_node = input_node

    while r_node and r_node.next:
        r_node = r_node.next.next
        l_node = l_node.next

        if r_node == l_node:
            l_node = input_node
            while 1:
                if l_node == r_node:
                    return r_node
                r_node = r_node.next
                l_node = l_node.next

    return None
