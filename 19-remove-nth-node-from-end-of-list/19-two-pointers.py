# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next

# Comment:
# 使用两个指针，fast先前进n步
# 接下来，slow 和 fast同时前进，当fast走到列表末尾时，slow走到倒数第n个节点的前一个(证明见下)
# 改变slow的下一个节点为下一个的下一个即可

# 假设原列表长度为m，fast从dummy走到末尾，一共走了m步，slow比fast少走了n步，
# 故slow走了(m-n)步，剩余n步走到末尾。即此时slow的后面有n个节点，故slow的下一个节点就是“倒数第n个节点”
# 故此时slow走到倒数第n个节点的前一个