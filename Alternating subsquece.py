test = int(input())
for _ in range(test):
    length = int(input())
    nums = list(map(int,input().split()))

    left = 0
    right = 0
    total = 0
    while right < length:
        elem = 0
        while right < length and nums[right] > 0:
            elem = max(elem,nums[right])
            right+=1

        total+=elem
        elem =float("-inf")
        while right < length and nums[right] < 0:
            elem = max(elem,nums[right])
            right+=1
        if elem != float("-inf"):
            total+=(elem)
    print(total)
