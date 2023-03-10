# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # depth = 0
        d = defaultdict(list)
        def traverse(root,val,depth):
            if not root:
                return 0

            d[depth].append(val)
            traverse(root.left, val * 2 , depth+1)
            traverse(root.right, (val * 2) + 1,depth+1)
        traverse(root,1,0)
        for key, val in d.items():
            ans = max(ans,val[-1]-val[0]+1)
        return ans