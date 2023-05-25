# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        dummy = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        # slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        maxi = 0
        while head.next and prev:
            maxi = max(maxi,head.val+prev.val)
            head = head.next
            prev = prev.next
        return maxi