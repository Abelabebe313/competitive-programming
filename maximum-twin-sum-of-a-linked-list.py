# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        stack = []
        length = 0
        i = 0
        while cur:
            stack.append(cur.val)
            length += 1
            cur = cur.next

        maxi = float('-inf')
        for i in range(length//2):
            maxi = max(maxi,stack[i]+stack.pop())
        return maxi