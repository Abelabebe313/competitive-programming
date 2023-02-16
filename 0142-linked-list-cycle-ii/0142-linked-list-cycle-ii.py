# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = curr =head
        flag = False
        if head and head.next:
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    flag = True
                    break
                    
            if flag:
                slow = head
                while slow:
                    if slow == fast:
                        break
                    slow = slow.next
                    fast = fast.next

                return slow
            return