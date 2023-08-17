import collections
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
         
        m, n = len(matrix), len(matrix[0])
        elements = collections.defaultdict(list)
        results = []
     
        for i in range(m):
            for j in range(n):
                elements[i+j].append(matrix[i][j])
                 
        for k, v in elements.items():
            if k % 2 == 0:
                results.extend(v[::-1])
            else:
                results.extend(v)
 
        return results