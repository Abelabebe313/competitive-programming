# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(input().split())
n = int(input())
newSet = set()
for i in range(n):
    temp = set(input().split())
    newSet = newSet.union(temp)
ans = setA.issuperset(newSet)

print(ans)
