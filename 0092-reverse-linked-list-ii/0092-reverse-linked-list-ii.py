# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        lookup = []
        while curr.next:
            lookup.append(curr.next)
            curr = curr.next
        lookup.insert(0,head)
        while left < right:
            lookup[left-1].val,lookup[right-1].val = lookup[right-1].val,lookup[left-1].val
            left += 1
            right -= 1
        return head