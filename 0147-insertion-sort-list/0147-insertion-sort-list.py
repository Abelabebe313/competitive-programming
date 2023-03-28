# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        
        while curr:
            prev = dummy
            next_node = dummy.next
            
            # Find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev = next_node
                next_node = next_node.next
            
            # Insert the current node into the sorted list
            next_curr = curr.next
            curr.next = next_node
            prev.next = curr
            curr = next_curr
        
        return dummy.next


        
        