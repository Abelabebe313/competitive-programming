t = int(input())
for operation in range(t):
    test = []
    garbage = input()
    for i in range(8):
        test.append(list(input()))
    
    for i in range(1,len(test)-1):
        for j in range(1,len(test[0])-1):
            if test[i][j] == '#':
                if test[i-1][j-1] == test[i-1][j+1] == test[i+1][j-1] == test[i+1][j+1] == '#':
                    print(f'{i+1} {j+1}')
                    break
    
