# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        
        len_A = 1
        while(pointerA.next):
            pointerA = pointerA.next
            len_A += 1
        pointerA = headA
        
        len_B = 1
        while(pointerB.next):
            pointerB = pointerB.next
            len_B += 1
        pointerB = headB

        step = 0
        while(pointerA != pointerB):
            if pointerA.next:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB.next:
                pointerB = pointerB.next
            else:
                pointerB = headA
            step += 1
            if step > len_A + len_B:
                return None
        return pointerA


# Comment:
# 为了避免计算长度，若判断条件仍为pointerA.next，即不让A,B 落在None,则
# 若A, B 不相交，则
# pointerA 遍历完A和B时，所走步数为(m-1) + 1 + (n-1), 落在B的最后一个元素
# pointerB 遍历完B和A时，所走步数为(n-1) + 1 + (m-1), 落在A的最后一个元素
# 判断 (pointerA != pointerB and pointerA.next == None and pointerB.next == None) 即可
# 注意 pointerA != pointerB 不能省略，因为极端情况，A，B在最后一个元素相交，此时
# 满足 pointerA.next == None and pointerB.next == None， 但同时pointerA == pointerB， 应该返回pointerA

# leetcode 中省略判断(pointerA != pointerB ) 仍可通过，测试样例不完全。
# 反例：
# 3
# [1,2,3]
# [4,3]
# 2
# 1


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
            if pointerA.next:
                pointerA = pointerA.next
            else:
                pointerA = headB
            if pointerB.next:
                pointerB = pointerB.next
            else:
                pointerB = headA
            if pointerA != pointerB and pointerA.next==None and pointerB.next==None:
                return None
        return pointerA
    
# Comment:
# 另一种写法，判断条件为if pointerA，而不是pointerA.next，即让pointerA和pointerB落在None，见160-be-None.py