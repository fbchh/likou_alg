"""
xxx
"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solve:
    def __init__(self):
        self.list_node_len = 0
        self.head = ListNode(None)

    def get(self, index):
        if index >= self.list_node_len:
            return -1
        cur = self.head.next
        inner_count = 0
        while cur:
            if inner_count == index:
                return cur.val
            cur = cur.next
            inner_count += 1

    def addAtHead(self, val):
        self.head.next = ListNode(val, self.head.next)
        self.list_node_len += 1

    def addAtTail(self, val):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.list_node_len += 1

    def addAtIndex(self, index, val):
        if index > self.list_node_len:
            return

        if index < 0:
            self.addAtHead(val)
        elif index == self.list_node_len:
            self.addAtTail(val)
        else:
            inner_count = 0
            cur = self.head.next
            last = self.head
            while cur:
                if inner_count == index:
                    last.next = ListNode(val, cur)
                    break

                last = cur
                cur = cur.next
                inner_count += 1
            self.list_node_len += 1

    def deleteAtIndex(self, index):
        if index >= self.list_node_len:
            return

        inner_count = 0
        cur = self.head.next
        last = self.head
        while cur:
            if inner_count == index:
                last.next = cur.next
                cur.next = None
                break
            last = cur
            cur = cur.next
            inner_count += 1
        self.list_node_len -= 1


def tst():
    tst_obj = Solve()
    tst_obj.addAtHead(1)
    tst_obj.addAtTail(3)
    tst_obj.addAtIndex(1, 2)
    tst_obj.get(1)
    tst_obj.deleteAtIndex(0)
    tst_obj.get(0)


if __name__ == "__main__":
    tst()
    ...
