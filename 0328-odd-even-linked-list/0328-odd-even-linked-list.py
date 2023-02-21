# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        cur = head
        eHead = even
        oHead=odd
        index = 1
        
        while cur:
            if index % 2 == 0:
                even.next = cur
                even = even.next
            elif index % 2 != 0:
                odd.next = cur
                odd = odd.next
            cur = cur.next
            index += 1  

        even.next = None
        odd.next = eHead.next
        return oHead.next
            
            