# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            prev = None
            current = root
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        def push(new_data, head):
            new_node = ListNode(new_data)
            new_node.next = head
            head = new_node
            return head

        head1 = reverse(l1)
        head2 = reverse(l2)

        cur1 = head1
        cur2 = head2

        newlist = None
        head = None
        rem = 0
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            total = val1 + val2 + rem

            if total < 10:
                head = push(total, head)
                rem = 0
            else:
                head = push(total - 10, head)
                rem = 1

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        if rem:
            head = push(rem, head)

        return head