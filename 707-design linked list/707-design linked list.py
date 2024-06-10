class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 > self.size:
            return -1
        cur_node = self.dummy_head
        for i in range(index + 1):
            cur_node = cur_node.next
        return cur_node.val
        
    def addAtHead(self, val: int) -> None:
        cur_head = self.dummy_head.next
        self.dummy_head.next = ListNode(val, next=cur_head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur_node = self.dummy_head
        for i in range(self.size):
            cur_node = cur_node.next
        cur_node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            cur_node = self.dummy_head
            for i in range(index):
                cur_node = cur_node.next
            cur_next = cur_node.next
            cur_node.next = ListNode(val, next = cur_next)
            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            cur_node = self.dummy_head
            for i in range(index):
                cur_node = cur_node.next
            cur_node.next = cur_node.next.next
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Comment: 在增加删除节点时，需要维护size的值
# 在deleteAtIndex时，移动次数为index，（range(index)，index=0时不移动）
# 移动index次，可以让从dummy_head移动到index的前一个节点，此时将该节点的next指向下一个节点(index节点)的next即可