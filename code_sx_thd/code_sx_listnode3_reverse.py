"""
xxx
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(head):
    cur = head
    tail_node = None
    while cur:
        next = cur.next
        cur.next = tail_node
        tail_node = cur
        cur = next

    return tail_node


if __name__ == "__main__":
    ...
