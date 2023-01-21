test = int(input())
for t in range(test):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    flag = True
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] <= 1:
            continue
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
