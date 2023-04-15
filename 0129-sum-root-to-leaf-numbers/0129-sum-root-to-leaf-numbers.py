# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def traverse(root,path):
            nonlocal nums
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val)
                nums.append(path)
                
            path += str(root.val)
        
            traverse(root.left,path)
            traverse(root.right,path)
            path = path[:-1]
        
        traverse(root,'')
        
        summ = 0
        for num in nums:
            summ += int(num)
        return summ
        