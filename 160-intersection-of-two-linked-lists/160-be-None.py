# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB

        while(pointerA != pointerB):
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA
        return pointerA
    

# 简化写法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB

        while(pointerA != pointerB):
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        return pointerA

# Comment:
# 当指针指向末尾时，可以将下一步指向None,
# 如此，若不相交，最终两个指针会同时指向None，结束循环，不用另外设置结束条件
# 证明：假设A的长度为m, B的长度为n，不相交。
# 当pointerA遍历完A和B时，所走步数为m + 1 + n, 即从headA走到A尾部的None,走到headB,最后落在B结尾的None
# 当pointerB遍历完A和B时，所走步数为n + 1 + m, 即从headB走到B尾部的None,走到headA,最后落在A结尾的None
# 此时pointerA == pointerB，结束循环返回None

# 另一种方法，不让A, B 落在None, 需要另外判断结束条件，见160-not-be-None.py