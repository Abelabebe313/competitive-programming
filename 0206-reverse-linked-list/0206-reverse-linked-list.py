# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lookup = []
        if not head:
            return None
        elif not head.next:
            return head
        else:
            while curr.next != None:
                lookup.append(curr.next)
                curr = curr.next
            lookup.insert(0,head)

            left = 0
            right = len(lookup)-1
            while left < right:
                lookup[left].val,lookup[right].val = lookup[right].val,lookup[left].val
                left += 1
                right -= 1
            return head