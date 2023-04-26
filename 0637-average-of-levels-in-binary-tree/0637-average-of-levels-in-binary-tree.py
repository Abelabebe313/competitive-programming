# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        queue = deque()
        queue.append(root)

        while queue:
            count = len(queue)
            summ = 0
            temp = []
            for node in queue:
                summ += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            avg.append(summ/count)
            queue = temp
        
        return avg
        
            