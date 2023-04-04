test = int(input())
for t in range(test):
    x = int(input())
    y = (x & (-x))
    while y & x == 0 or y==x:
        y += 1
    print(y)