"""
代码随想录学习记录
章节：栈与队列
题目：用队列实现栈

    题意：
    使用队列实现栈的下列操作：
    push(x) -- 元素 x 入栈
    pop() -- 移除栈顶元素
    top() -- 获取栈顶元素
    empty() -- 返回栈是否为空

    注意:
    你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
    你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
    你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class DataStack:

    def __init__(self):
        self.input_list = []
        self.output = None

    def push(self, e):
        self.input_list.append(e)

    def _trans(self):
        # 满足输出队列为空
        self.output = self.input_list[-1]
        self.input_list = self.input_list[:-1]

    def pop(self):
        if not self.is_empty():
            if self.output is None:
                self._trans()
            _res = self.output
            self.output = None
            return _res

    def peek(self):
        if not self.is_empty():
            if self.output is None:
                self._trans()
            return self.output

    def is_empty(self):
        return len(self.input_list) == 0 and self.output is None


if __name__ == "__main__":

    _stack1 = DataStack()
    _stack1.push(1)
    _stack1.push(11)
    _stack1.push(111)

    print(_stack1.is_empty())

    print(_stack1.peek())
    _stack1.pop()

    print(_stack1.is_empty())
    _stack1.push(222)

    print(_stack1.peek())
    _stack1.pop()

    print(_stack1.peek())
    _stack1.pop()

    print(_stack1.is_empty())
    pass
