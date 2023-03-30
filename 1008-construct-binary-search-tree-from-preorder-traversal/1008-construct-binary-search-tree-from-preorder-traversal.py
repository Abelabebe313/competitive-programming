# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def construct_BST(lst):
            if not lst:
                return None
            
            root = TreeNode(lst[0])
            i = 1
            while i < len(lst) and lst[i] < root.val:
                i += 1
            root.left = construct_BST(lst[1:i])
            root.right = construct_BST(lst[i:])
            
            return root
        
        return construct_BST(preorder)
        