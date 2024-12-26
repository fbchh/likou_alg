"""
xxx
"""


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solve(head, n):
    head = ListNode(None, head)
    cur = head

    inner_arr = []
    while cur:
        inner_arr.append(cur)
        cur = cur.next

    inner_arr.append(None)
    idx = len(inner_arr) - 1 - n
    inner_arr[idx - 1].next = inner_arr[idx + 1]

    return head.next


def tst():
    def arr2list_node(arr):
        head = ListNode(None)
        cur = head
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return head.next

    print(solve(arr2list_node([1, 2, 3, 4, 5]), 2))


if __name__ == "__main__":
    tst()
