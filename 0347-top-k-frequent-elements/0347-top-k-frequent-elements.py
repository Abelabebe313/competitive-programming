class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        heap = []
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans