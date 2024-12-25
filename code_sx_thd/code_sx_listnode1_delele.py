"""
xxx
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(head, val):
    head = ListNode(None, head)
    cur = head
    last = head

    while cur:
        if cur.val == val:
            last.next = cur.next
            cur.next = None
            cur = last.next
        else:
            last = cur
            cur = cur.next

    return head.next


def tst():
    def build_list_node(arr):
        head = ListNode(None)
        cur = head
        for e in arr:
            new_node = ListNode(e)
            cur.next = new_node
            cur = cur.next

        return head.next

    print(solve(build_list_node([1, 2, 6, 3, 4, 5, 6]), 6))
    print(solve(build_list_node([]), 1))
    print(solve(build_list_node([7, 7, 7, 7]), 7))


if __name__ == "__main__":
    tst()
    ...
