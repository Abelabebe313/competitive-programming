class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowlist = set()
        collist = set()
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] != 0:
                    continue
                elif matrix[m][n] == 0:
                    rowlist.add(m)
                    collist.add(n)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowlist:
                    matrix[i][j] = 0
                elif j in collist:
                    matrix[i][j] = 0
        
            
        
                    
    
       
        