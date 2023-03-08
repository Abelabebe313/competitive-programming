# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        if len(nums) == 1:
            return TreeNode(nums[-1])
        
        mid = (len(nums)-1)//2
        newBST = TreeNode(nums[mid])
        newBST.left = self.sortedArrayToBST(nums[:mid])
        newBST.right = self.sortedArrayToBST(nums[mid+1:])
        
        return newBST