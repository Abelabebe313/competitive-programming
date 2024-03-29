# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current_node = head
        
        while current_node is not None:
            stack.append(current_node.val)
            current_node = current_node.next
        return stack == stack[::-1]