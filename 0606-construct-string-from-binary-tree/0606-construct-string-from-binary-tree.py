# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = []
        def recur(root):
            nonlocal path
            if not root:
                return
                
            path.append('(')
            path.append(str(root.val))
            if not root.left and root.right:
                path.append('()')
            recur(root.left)
            recur(root.right)
            path.append(')')
        recur(root)
        return (''.join(path[1:-1]))