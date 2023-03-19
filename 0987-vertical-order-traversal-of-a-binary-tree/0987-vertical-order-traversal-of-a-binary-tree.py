import bisect
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
         
            order = defaultdict(list)
            def travesr(root,row,col):
                if not root:
                    return
                order[col].append([row,root.val])
                # bisect.insort(order[col], root.val)
                travesr(root.left,row+1,col-1)
                travesr(root.right,row+1,col+1)
            travesr(root,0,0)
            
            ans = []
            # print(order)
            for key in sorted(order.keys()):
                temp = []
                for j in sorted(order[key]):
                    temp.append(j[1])
                    
                ans.append(temp)
            return ans