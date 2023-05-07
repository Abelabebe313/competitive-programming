# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = []
        
        for i in range(len(lists)):
            node = lists[i]
            if lists[i]:
                heappush(heap,(node.val,i))
                lists[i] = lists[i].next
                
        dummy = ListNode()
        cur = dummy
        
        while heap:
            node, idx = heappop(heap)
            cur.next = ListNode(node)
            cur = cur.next
            
            if lists[idx]:
                heappush(heap,(lists[idx].val,idx))
                lists[idx] = lists[idx].next
        return dummy.next
            