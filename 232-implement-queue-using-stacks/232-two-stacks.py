class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        for ele in self.stack2[::-1]:
            self.stack1.append(ele)
        self.stack1.append(x)
        self.stack2 = []
        for ele in self.stack1[::-1]:
            self.stack2.append(ele)
        self.stack1 = [] 
        self.size += 1

    def pop(self) -> int:
        val = self.stack2[-1]
        self.stack2 = self.stack2[:-1]
        self.size -= 1
        return val

    def peek(self) -> int:
        val = self.stack2[-1]
        return val

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()