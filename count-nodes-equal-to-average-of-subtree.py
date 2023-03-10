# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        total = 0
        count = 0
        def total_finder(root):
            nonlocal total,count
            if not root:
                return
            total += root.val
            count += 1 
            total_finder(root.left)
            total_finder(root.right)
            return [total,count]
        
        def traverse(node):
            nonlocal ans,total,count
            if not node:
                return
            
            t,c = total_finder(node)
            if (t//c) == node.val:
                ans += 1
            total = 0
            count = 0
            traverse(node.left)
            traverse(node.right) 
        traverse(root)
        return ans