# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while(True):
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            if slow and slow.next:
                slow = slow.next
            else:
                return None
            if slow == fast:
                break
        slow = head
        while(slow != fast):
            fast = fast.next
            slow = slow.next
        return slow
# Comment:
# 设head到环入口长度为n, slow进入环中后走s步与fast相遇

# 当slow 和 fast 在环中相遇时
# slow在环中走的距离为s, fast在环中走的距离为2s + n
# 故 s % m = (2s + n) % m, 即 (s + n) % m = 0
# 故再走n步即可到达环入口，再走n步的计数是将slow指针移到head。同时移动fast和slow，每次都只走一步。
# 则fast和slow再次相遇时，slow走n步到达入口，fast走n步到达入口，故相遇，slow起到了计数的作用。

# 时间复杂度 O(n), n为链表长度
# 原因：slow步数不可能超过2n

# 空间复杂度 O(1)

#简洁写法：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow
        return None