# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = []
        def BFS(root):
            nonlocal avg
            queue = deque()
            queue.append(root)
            
            while queue:
                count = len(queue)
                summ = 0
                for i in range(len(queue)):
                    node = queue.popleft()
                    summ += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                avg.append(summ/count)
        BFS(root)
        return avg
        
            