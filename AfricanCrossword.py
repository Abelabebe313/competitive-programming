from collections import Counter
order = list(map(int,input().split()))
row = order[0]
col = order[1]
rowDic = [{}] * row
colDic = [{}] * col

matrix = []
for i in range(row):
    matrix.append(list(input()))
    rowDic[i] = Counter(matrix[-1]) 

for i in range(col):
    colDic[i] = Counter(list(zip(*matrix))[i])

for i in range(row):
    for j in range(col):
        if rowDic[i][matrix[i][j]] == 1 and colDic[j][matrix[i][j]] == 1:
            print(matrix[i][j],end="")

