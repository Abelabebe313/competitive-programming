# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = 0
        def traverse(root,pathSum):
            nonlocal ans
            if not root:
                return
            # print(root.val,path)
            pathSum += root.val
            ans += prefix[pathSum-targetSum]
            prefix[pathSum] += 1
            
            traverse(root.left,pathSum)
            traverse(root.right,pathSum)
            prefix[pathSum] -= 1
            
        traverse(root,0) 
        return ans     