class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.size = 0

    def push(self, x: int) -> None:
        for ele in self.queue2:
            self.queue1.append(ele)
        self.queue2 = []
        self.queue2.append(x)
        for ele in self.queue1:
            self.queue2.append(ele)
        self.queue1 = []
        self.size += 1

    def pop(self) -> int:
        val = self.queue2[0]
        self.queue2 = self.queue2[1:]
        self.size -= 1
        return val

    def top(self) -> int:
        val = self.queue2[0]
        return val

    def empty(self) -> bool:
        return self.size == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()