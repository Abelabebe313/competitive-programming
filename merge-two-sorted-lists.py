# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:   
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Node = ListNode()
        self.recursion(list1,list2,Node)
        return Node.next
    
    def recursion(self, lis1, lis2, Node): 

        if not lis1 and not lis2:
            return Node

        if not lis1:
            Node.next = lis2
            self.recursion(lis1,lis2.next,Node.next)
        elif not lis2:
            Node.next = lis1
            self.recursion(lis1.next,lis2,Node.next)

        elif not lis2 or lis1.val <= lis2.val:
            Node.next = lis1
            self.recursion(lis1.next, lis2, Node.next)
        elif not lis1 or lis1.val > lis2.val:
            Node.next = lis2
            self.recursion(lis1, lis2.next, Node.next)