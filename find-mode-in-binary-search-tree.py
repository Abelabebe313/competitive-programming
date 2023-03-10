# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict()
        ans = []
        def traverse(root):
            nonlocal d
            if not root:
                return None
            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        
        print(d)

        maxi = max(d.values())
        max_key = []
        for key,val in d.items():
            if val == maxi:
                max_key.append(key)
        return max_key

        # if not ans:
        #     return lst
        # return ans
        # return [max(arr,key=arr.count)]