from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        flag = True
        
        rowDict = [{}] * row 
        colDict = [{}] * col
        
        for i in range(row):
            rowDict[i] = Counter(board[i])
            
        for i in range(col):
            colDict[i] = Counter(list(zip(*board))[i])
        
        for i in range(0,row,3):
            for j in range(0,col,3):
                check = []
                for roww in range(i,i+3):
                    for coll in range(j,j+3):
                        if board[roww][coll] != '.':
                            # if board[roww][coll] in check:
                            #     break
                            if board[roww][coll] not in check:
                                check.append(board[roww][coll])
                            else:
                                flag = False
                print(flag)
                
        if flag:
            for i in range(row):
                for j in range(col):
                    if board[i][j] != '.' and (rowDict[i][f'{board[i][j]}'] > 1 or colDict[j][f'{board[i][j]}'] > 1):
                        flag = False
                        break
        return flag