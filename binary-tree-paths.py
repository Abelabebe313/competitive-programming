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
            if not root:
                return
            if  not root.left and not root.right:
                # print(root.val,string)
                output.append("->".join(list(map(str,string))))
                return  
            if root.left:
                string.append(root.left.val)
                traverse(root.left,string)
                string.pop()
            if root.right:
                string.append(root.right.val)
                traverse(root.right,string)
                string.pop()
        
        traverse(root,[root.val])
        return output