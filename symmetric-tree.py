# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(rootL,rootR):
            if not rootL and not rootR:
                return True
            if (not rootL and rootR) or (rootL and not rootR):
                return False
            if rootL.val != rootR.val:
                return False
                
            Left = check(rootL.left,rootR.right)
            Right = check(rootL.right,rootR.left)
            return Left and Right
        return check(root.left, root.right)