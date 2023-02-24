# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        
        maxx = float('-inf')
        ans = []
        listt = []
        maxStack = []
        
        while cur:
            listt.append(cur.val)
            cur = cur.next
            
        for i in range(len(listt)-1, -1, -1):
            # validate
            while maxStack and listt[i] >= maxStack[-1]:
                maxStack.pop()

            # append to answer
            if maxStack:
                ans.append(maxStack[-1])
            else:
                ans.append(0)

            # append to stack
            maxStack.append(listt[i])
                
                

        return ans[::-1]