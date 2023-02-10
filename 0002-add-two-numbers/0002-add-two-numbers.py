# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumOne = []
        sumTwo = []
        def reverse(start):
            curr = start
            prev = None
            follow = curr.next
            
            while curr:
                curr.next = prev
                prev = curr
                curr = follow
                if follow:
                    follow = follow.next
            start = prev
            return start
        def converter(start,output):
            while start:
                output.append(start.val)
                start = start.next
            
        list1 = reverse(l1)
        list2 = reverse(l2)
        
        converter(list1,sumOne)
        converter(list2,sumTwo)
        num1 = int("".join(map(str,sumOne)))
        num2 = int("".join(map(str,sumTwo)))
        result = num1 + num2
        newlist = list(map(int,str(result)))
        newlist.reverse()
        head = ListNode(newlist[0])
        cur = head
        for i in newlist[1:]:
            node = ListNode(i)
            cur.next = node
            cur = cur.next
        return head
            
        