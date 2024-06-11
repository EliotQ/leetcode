# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre, cur = dummy, head

        while(cur and cur.next):
            temp = cur.next.next
            pre.next = cur.next
            pre.next.next = cur
            cur.next = temp

            pre = cur
            cur = cur.next
        return dummy.next

# Comment, 想象交换过程，0->2, 2->1, 1->3
# 进行的条件：当前节点（已交换部分的末尾）和下一个节点都不为空（未交换部分的头）
# 因为1)若当前节点为空，则当前节点的上一个节点为结尾，停止；2)若下一个结点为空，则当前节点为结尾，停止
# 时间复杂度O(n)
# 空间复杂度O(1)