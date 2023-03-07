# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if not p  and q:
            return False 
        if p and not q:
            return False
        if p and q and p.val != q.val:
            return False
        
        Left = self.isSameTree(p.left, q.left)
        Right = self.isSameTree(p.right, q.right)
       

        return Left and Right
        
        # p_hash = defaultdict()
        # q_hash = defaultdict()
        
        # def insert_p_to_hash(root):
        #     if root == None:
        #         return
        #     insert_p_to_hash(root.left)
        #     if root.left:
        #         p_hash[root.val] = 'left'
        #     else:
        #         p_hash[root.val] = 'right'
        #     insert_p_to_hash(root.right)
        
        # def insert_q_to_hash(root):
        #     if root == None:
        #         return
        #     insert_q_to_hash(root.left)
        #     if root.left:
        #         q_hash[root.val] = 'left'
        #     else:
        #         q_hash[root.val] = 'right'
        #     insert_q_to_hash(root.right)
        # insert_p_to_hash(p)
        # insert_q_to_hash(q)

        # def maxDepth(root):
        #     if not root:
        #         return 0
        #     left = maxDepth(root.left)
        #     right = maxDepth(root.right) 

        #     return max(left,right) + 1
        # # print(maxDepth(p))
        # if p_hash == q_hash and maxDepth(p) == maxDepth(q):
        #     return True
        # else:
        #     return False