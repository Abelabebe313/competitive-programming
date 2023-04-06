from collections import defaultdict
n = int(input())
source = []
sink = []
vrtx = defaultdict(list)


for i in range(n):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            vrtx[i+1].append(j+1)
        
    print(len(vrtx[i+1]),*vrtx[i+1])






