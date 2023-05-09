class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
            heappush(heap,((nums1[i]+nums2[0]),i,0))
        ans = []
        
        while heap and len(ans)<k:
            summ,n1,n2 = heappop(heap)
            ans.append([nums1[n1],nums2[n2]])
            if n2 < len(nums2)-1:
                heappush(heap,((nums1[n1]+nums2[n2+1]),n1,n2+1))
        return ans