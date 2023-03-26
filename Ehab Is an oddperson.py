item = int(input())
arr = list(map(int,input().split()))
even = odd = False
for num in arr:
    if (num % 2) == 0:
        even = True
    else:
        odd = True

if even and odd:
    arr.sort()
    print(*arr)
else:
    print(*arr)
