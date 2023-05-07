# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1,l2):
            dummy = ListNode()
            curr = dummy
            
            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next
            if l1:
                curr.next = l1
            
            if l2:
                curr.next = l2
            return dummy.next
        
        if not lists and len(lists)==0:
            return None
        while len(lists) > 1:
            newList = []
            
            for i in range(0,len(lists),2):
                lis1 = lists[i]
                lis2 = lists[i+1] if (i+1) < len(lists) else None
                newList.append(merge(lis1,lis2))
        
            lists = newList
        return lists[0]
        
        
            