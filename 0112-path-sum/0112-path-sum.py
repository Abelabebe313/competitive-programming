# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(root,pathSum):
            if not root:
                return False
            pathSum+= root.val
            if not root.left and not root.right:
                return pathSum == targetSum
        
            return traverse(root.left,pathSum) or traverse(root.right,pathSum)
            
        return traverse(root,0) if root else False