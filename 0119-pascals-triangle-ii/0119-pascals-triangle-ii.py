class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}
        def recursive(row, col):
            if col == 0 or row==col or  row==0 or  row == 1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row, col)] =  (recursive(row-1,col - 1) + recursive(row-1, col))
            return memo[(row, col)]
        
        answer = []
        for col in range(rowIndex+1):
            answer.append(recursive(rowIndex, col))
        return answer
            