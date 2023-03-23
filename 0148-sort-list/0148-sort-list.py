# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if not head.next:
            return head
        
        list1 , list2 = self.split(head)
        return self.merge(self.sortList(list1),self.sortList(list2))
    
    def split(self,head):
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return head, head2
    
    def merge(self,list1,list2):
        Node = temp = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                
        while list1:
            temp.next = list1
            list1 = list1.next
            temp = temp.next
            
        while list2:
            temp.next = list2
            list2 = list2.next
            temp = temp.next
        return Node.next
            
            
            
            