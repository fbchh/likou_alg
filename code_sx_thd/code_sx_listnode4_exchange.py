"""
xxx
"""


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(head):
    head = ListNode(None, head)

    cur = head.next
    last = head

    while cur and cur.next:
        next = cur.next
        next_next = cur.next.next

        cur.next = next_next
        next.next = cur
        last.next = next

        last = cur
        cur = next_next
    return head.next


def tst():
    def arr2list_node(arr):
        head = ListNode(None)
        cur = head
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return head.next

    print(solve(arr2list_node([1, 2, 3, 4])))


if __name__ == "__main__":
    tst()
