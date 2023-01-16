class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visted = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i, j) not in visted:
                    matrix[i][j] ,matrix[j][i] = matrix[j][i] ,matrix[i][j]
                    visted.add((i,j))
                    visted.add((j,i))
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)