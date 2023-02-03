# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        trav = head
        length = 1
        
        
        if not head:
            return None
        elif not head.next:
            return head
        else:
            while trav.next:
                trav = trav.next
                length += 1
        
            k = k % length
            
            while k > 0:
                while curr.next:
                    sec_last = curr
                    curr = curr.next
                sec_last.next = None
                curr.next = head
                head = curr
    
                k -= 1
            return head