"""
代码随想录学习记录
章节：链表
题目:设计链表

    题意：

    在链表类中实现这些功能：
    get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。
                        如果 index 等于链表的长度，则该节点将附加到链表的末尾。
                        如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""
from time import time


def count_time(input_process, *input_params1, **input_params2):
    if callable(input_process):
        t1 = time()
        res = input_process(*input_params1, **input_params2)
        print(f"tol cost sec: {time() - t1}S")
        return res
    else:
        print("[error] input process must be callable")


class ListNode:

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyList:

    def __init__(self, val=None, next=None):
        self.node = ListNode(val, next)
        self.size = 1

    def get(self, index):
        if self.size - 1 < index:
            return -1
        cur_node = self.node
        _count = 0  # 起始节点
        while 1:
            if _count == index:
                return cur_node.val
            cur_node = cur_node.next
            _count += 1

    def add_head(self, val):
        head_node = ListNode(val)
        head_node.next = self.node
        self.node = head_node
        self.size += 1

    def add_tail(self, val):
        tail_node = ListNode(val)
        cur_node = self.node
        while 1:
            if cur_node.next is None:
                cur_node.next = tail_node
                self.size += 1
                break
            cur_node = cur_node.next

    def add_index(self, index, val):
        if index == self.size:
            self.add_tail(val)
        elif index <= 0:
            self.add_head(val)
        elif 0 < index < self.size:
            _count = 0
            cur_node = self.node
            while 1:
                if _count == index - 1:
                    mid_node = cur_node.next
                    new_node = ListNode(val, mid_node)
                    cur_node.next = new_node
                    self.size += 1
                    break
                cur_node = cur_node.next
                _count += 1

    def deleteAtIndex(self, index):
        if 0 <= index < self.size:
            _count = -1
            v_head_node = ListNode(None)
            v_head_node.next = self.node
            cur_node = v_head_node
            while 1:
                if _count == index - 1:
                    after_node = cur_node.next.next if cur_node.next.next else None
                    cur_node.next = after_node
                    self.size -= 1
                    break
                cur_node = cur_node.next
                _count += 1
            self.node = v_head_node.next


if __name__ == "__main__":
    def tst1():
        list_node1 = MyList()
        print(list_node1.get(0))
        list_node1.add_head(0)
        list_node1.add_tail(2)
        list_node1.add_index(0, -1)
        list_node1.add_index(4, 3)
        list_node1.add_index(1, 0.5)
        list_node1.deleteAtIndex(0)
        print(list_node1.get(3))


    count_time(tst1)
