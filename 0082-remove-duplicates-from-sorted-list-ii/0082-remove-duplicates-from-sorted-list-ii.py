# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = ListNode()
        ans = prev
        prev.next = curr
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
                curr=curr.next
                continue
            prev=curr
            curr = curr.next
        return ans.next