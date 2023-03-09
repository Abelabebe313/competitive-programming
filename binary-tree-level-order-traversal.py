# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)

        def levelTraverse(root, depth):
            if not root:
                return None
            d[depth].append(root.val)
            levelTraverse(root.left, depth+1)
            levelTraverse(root.right, depth+1)
        levelTraverse(root, 0)
        ans = []
        for key,val in d.items():
            ans.append(val)
        return ans