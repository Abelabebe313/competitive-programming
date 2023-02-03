# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = head
        total = 1
        if not head:
            return None
        elif not head.next:
            head = None
            return head
        else:
            while dummy.next:
                dummy = dummy.next
                total += 1
            
            index = 0
            iteration = total - n -1 
            if iteration >= 0:
                while curr.next and index < iteration:
                    curr = curr.next
                    index += 1
                temp = curr.next.next
                curr.next = temp
            else:
                head = head.next

            return head

            