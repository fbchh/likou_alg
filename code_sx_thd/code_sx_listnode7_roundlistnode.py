"""
xxx
"""


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve1(head):
    # 官方方法
    cur = head
    fast = head
    while fast and fast.next:
        cur = cur.next
        fast = fast.next.next
        if cur == fast:
            cur1 = head
            while cur != cur1:
                cur = cur.next
                cur1 = cur1.next
            return cur

    return None


if __name__ == "__main__":
    tst_list_node = ListNode(1)
    tst_list_node1 = ListNode(1)
    print(str(tst_list_node), str(tst_list_node1))
    """
    这里自定义的class在实例化一个对象的时候会有一个带有类似内存位置的一个类型（eg:"<__main__.ListNode object at 0x0000018E6B34D040>"），
    将其str强制类型转换后，可当做dict的key，然后采用计数的方法也可以对本题进行求解，但是leetcode中打印链表节点并没有前面说的特征
    """
    ...
