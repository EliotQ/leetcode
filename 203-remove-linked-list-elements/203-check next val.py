# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        cur = dummy

        while(cur.next):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
    
# Comment:
# 1. Create a dummy node to handle the case when the head node is the target value.
# 2. 在while循环中，判断当前节点的下一个节点是否为目标值：
#    如果是，将当前节点的下一个节点指向下下个节点，当前节点不动，在下一次循环中继续判断当前节点的下一个节点；
#    如果不是，将当前节点指向下一个节点，在下一次循环中继续判断当前节点的下一个节点。