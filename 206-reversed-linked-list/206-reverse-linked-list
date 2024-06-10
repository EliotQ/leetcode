# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head

        while(cur):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# Comment: 
# 开始时，pre指向None，cur指向head
# 步骤：记cur.next, 改cur.next，改pre，改cur