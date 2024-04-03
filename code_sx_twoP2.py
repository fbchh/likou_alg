"""
代码随想录学习记录
章节：双指针
题目：环形链表II

    题意：
    题意： 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    说明：不允许修改给定的链表。
"""


def solve1(input_node):
    """
    解法1，二刷自己没有想起来双指针的写法以及思想
    :param input_node: xx
    :return: xx
    """
    s = input_node
    f = input_node
    while f and f.next:
        f = f.next.next
        s = s.next

        if s == f:
            s = input_node
            while 1:
                if s == f:
                    return s
                s = s.next
                f = f.next
    return None


if __name__ == "__main__":
    # 一刷的写法 不再测试
    pass
