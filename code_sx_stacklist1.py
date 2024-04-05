"""
代码随想录学习记录
章节：栈与队列
题目：用栈实现队列

    题意：
    使用栈实现队列的下列操作：

    push(x) -- 将一个元素放入队列的尾部。
    pop() -- 从队列首部移除元素。
    peek() -- 返回队列首部的元素。
    empty() -- 返回队列是否为空。

    你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
    假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
"""


# 自定义栈
class DataStack:

    def __init__(self):
        self.list = []

    def push(self, e):
        self.list.append(e)

    def pop(self):
        _res = self.list[-1]
        self.list = self.list[:-1]
        return _res

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def is_empty(self):
        return len(self.list) == 0


class DataList:

    def __init__(self):
        self.input_list = DataStack()
        self.output_list = DataStack()

    def _trans(self):
        # 满足输出栈为空的情况
        for _ in range(self.input_list.size()):
            self.output_list.push(self.input_list.pop())

    def push(self, e):
        self.input_list.push(e)

    def pop(self):
        if self.output_list.is_empty():
            self._trans()
        return self.output_list.pop()

    def peek(self):
        if self.output_list.is_empty():
            self._trans()
        return self.output_list.peek()

    def is_empty(self):
        return self.input_list.size() + self.output_list.size() == 0


if __name__ == "__main__":

    # _stack1 = DataStack()
    # _stack1.push(12)
    # _stack1.push(11)
    # _stack1.push(0.9)
    #
    # print(_stack1.peek())
    # _stack1.pop()
    # print(_stack1.size())
    # print(_stack1.is_empty())

    _list1 = DataList()
    _list1.push(1)
    _list1.push(11)
    _list1.push(111)

    print(_list1.is_empty())

    print(_list1.peek())
    _list1.pop()
    print(_list1.peek())
    _list1.pop()
    print(_list1.peek())
    _list1.pop()

    print(_list1.is_empty())
    pass
