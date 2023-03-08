# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def InOrder_trv(root):
            if not root:
                return []
            InOrder_trv(root.left)
            arr.append(root.val)
            InOrder_trv(root.right)
            return arr
        InOrder_trv(root)
        # print(arr)
        # count = 0
        # for idx in range(len(arr)):
        #     if num <= k:
        #         count += 1
        # return count
        return arr[k-1]