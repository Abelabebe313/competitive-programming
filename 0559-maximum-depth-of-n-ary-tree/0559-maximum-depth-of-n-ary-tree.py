"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def DFS(root):
            if len(root.children)==0:
                return 1
            depth = []
            
            for child in root.children:
                depth.append(DFS(child))
            return max(depth) + 1
        
        
        if not root:
            return 0
        return DFS(root)
            
        