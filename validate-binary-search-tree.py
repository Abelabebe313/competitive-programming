# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def InOrder_trv(root):
            if not root:
                return []
            InOrder_trv(root.left)
            arr.append(root.val)
            InOrder_trv(root.right)
            return arr
        InOrder_trv(root)
        
        is_sorted = all(a < b for a, b in zip(arr, arr[1:]))
        if is_sorted:
            return True
        else:
            return False