# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def traverse(root, string):
            if not root.left and not root.right:
                string += str(root.val)
                output.append(string)
                return None
            if not root.left:
                string += str(root.val) + '->'
                traverse(root.right, string)
                return None
            if not root.right:
                string += str(root.val) + '->'
                traverse(root.left, string)
                return None
            string += str(root.val) + '->'
            if root.left:
                traverse(root.left, string)
                
            if root.right:
                traverse(root.right, string)
                
        
        traverse(root,'')
        return output