order = list(map(int,input().split()))
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
 
ans = []
ptr1 = 0
ptr2 = 0
while ptr1 < len(nums1) and ptr2 < len(nums2):
    if nums1[ptr1] < nums2[ptr2]:
        ans.append(nums1[ptr1])
        ptr1 += 1
    else:
        ans.append(nums2[ptr2])
        ptr2 += 1
if ptr1 < len(nums1):
    while ptr1 < len(nums1):
        ans.append(nums1[ptr1])
        ptr1 += 1
if ptr2 < len(nums2):
    while ptr2 < len(nums2):
        ans.append(nums2[ptr2])
        ptr2 += 1
 
print(*ans)
