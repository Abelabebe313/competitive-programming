t = int(input())
for i in range(t):
    rec1 = list(map(int,input().split()))
    rec2 = list(map(int,input().split()))

    maxRec1 = max(rec1)
    if maxRec1 in rec2:
        rec1.remove(maxRec1)
        rec2.remove(maxRec1)
        summ = rec1[0] + rec2[0]
        if summ == maxRec1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")    
