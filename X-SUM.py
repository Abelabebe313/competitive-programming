t = int(input())
for operation in range(t):
    order = list(map(int,input().split()))
    matrix = []
    for i in range(order[0]):
        row = list(map(int,input().split()))
        matrix.append(row)

    maxSum = float("-inf")

    leftSum = {}
    rightDiff = {}
    for row in range(order[0]):
        for col in range(order[1]):
            leftSum[row + col] = matrix[row][col] + leftSum.get(row+col,0)
            rightDiff[row - col] = matrix[row][col] + rightDiff.get(row-col,0)
    
    for i in range(order[0]):
        for j in range(order[1]):
            maxSum = max(maxSum, (leftSum[i+j] + rightDiff[i-j] - matrix[i][j]))
    print(maxSum)
