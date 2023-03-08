# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True
        def traverse(root):
            nonlocal isBalance
            if not root:
                return 0
            Left = traverse(root.left)
            Right = traverse(root.right) 

            if abs(Left - Right) > 1:
                isBalance = False
            return max(Left , Right) + 1
                    
        traverse(root)
        return isBalance
            