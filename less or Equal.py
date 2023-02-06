n,k = list(map(int,input().split()))
nums = list(map(int,input().split()))
nums.sort()


res = nums[k-1]
if k == 0:
    res = nums[0]-1
    
count = 0
for i in nums:
    if i<=res:
        count+=1

if count!=k or res<1:
    print(-1)
else:
    print(res)
