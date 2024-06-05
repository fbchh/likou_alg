"""
xxx
"""


# 单向链表
class ListNode1:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# 双向链表
class ListNode2:
    def __init__(self, l=None, val=None, r=None):
        self.l = l
        self.val = val
        self.r = r


if __name__ == "__main__":
    # list_node1 = ListNode2(val=12, r=ListNode1(val=24))
    # print(list_node1)
    pass
