class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = len(matrix[0]) - 1
        mid = 0
        targetRow = 0
        for i in range(rows):
            if target > matrix[i][-1]:
                continue
            elif target < matrix[i][-1]:
                targetRow = i
                break
            else:
                return True
        
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[targetRow][mid] > target:
                right = mid -1
            elif matrix[targetRow][mid] < target:
                left = mid +1
            else:
                return True
        return False
                
            
        