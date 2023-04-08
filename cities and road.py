from collections import defaultdict
n = int(input())
road = 0

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            road += 1
print(road//2)
       
