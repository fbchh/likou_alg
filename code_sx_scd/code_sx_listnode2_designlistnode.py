"""
xxx
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class ListNode1:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index >= 0:
            if index < self.size:
                cur = self.head
                count = 0
                while cur:
                    if count == index:
                        return cur.val
                    cur = cur.next
                    count += 1
        return -1

    def add_head(self, val):
        self.head = ListNode(val=val, next=self.head)
        self.size += 1

    def add_tail(self, val):
        new = ListNode(val=val)
        cur = self.head
        if cur:
            while 1:
                if not cur.next:
                    cur.next = new
                    break
                cur = cur.next
        else:
            self.head = new
        self.size += 1

    def add_index_val(self, index, val):
        if index <= self.size:
            if index <= 0:
                self.add_head(val=val)
            elif index == self.size:
                self.add_tail(val=val)
            else:
                new = ListNode(val=val)
                cur = self.head
                count = 0
                while cur:
                    if count + 1 == index:
                        r_old = cur.next
                        cur.next = new
                        new.next = r_old
                        break
                    count += 1
                    cur = cur.next
            self.size += 1

    def del_index(self, index):
        if index >= 0:
            if self.size > index:
                if index == 0:
                    self.head = self.head.next
                    self.size -= 1
                else:
                    count = 0
                    cur = self.head
                    while count < self.size:
                        if count + 1 == index:
                            tgt_node = cur.next
                            if tgt_node:
                                cur.next = tgt_node.next
                                tgt_node.next = None
                            else:
                                cur.next = None
                            break
                        cur = cur.next
                        count += 1
                    self.size -= 1


if __name__ == "__main__":

    tst1 = ListNode1()

    tst1.add_head(1)
    tst1.add_tail(3)
    tst1.add_index_val(1, 2)
    print(tst1.get(1))
    tst1.del_index(1)
    print(tst1.get(1))
    print(tst1.get(3))
    tst1.del_index(3)
    tst1.del_index(0)
    print(tst1.get(0))
    tst1.del_index(0)
    print(tst1.get(0))

    pass


"""
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
"""