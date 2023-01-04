# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

dictA = defaultdict(list)

n, m = map(int,input().split())

for i in range(n):
    dictA[input()].append(str(i+1))
    
for index in range(m):
    groupB = input()
    if dictA[groupB]:
        print(' '.join(dictA[groupB]))
    else:
        print(-1)
        

        
