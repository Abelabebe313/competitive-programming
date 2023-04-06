from collections import defaultdict

n = int(input())
k = int(input())
Adj = defaultdict(list)

def AddEdge(u,v):
    Adj[u].append(v)
    Adj[v].append(u)   

for i in range(k):
    row = list(map(int,input().split()))
    if row[0] == 1:
        AddEdge(row[1],row[2])
    else:
        for val in Adj[row[1]].element():
            print(val,end=" ")
        print()
