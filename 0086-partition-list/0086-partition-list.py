# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        small = dummyNode
        large = ListNode()
        larg = large
        
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                larg.next = head
                larg = larg.next
            head = head.next
        
        larg.next = None
        small.next = large.next
        return dummyNode.next