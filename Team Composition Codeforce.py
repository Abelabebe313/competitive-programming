test = int(input())
for t in range(test):
    a , b = list(map(int,input().split()))
    new = (a + b)//4
    ans = min(a,b,new)
    print(ans)