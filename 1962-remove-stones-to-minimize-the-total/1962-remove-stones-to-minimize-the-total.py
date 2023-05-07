class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-num for num in piles]
        
        heapify(piles)
        for i in range(k):
            temp = -heappop(piles)
            temp = temp - floor(temp/2)
            heappush(piles,-temp)
            
        return abs(sum(piles))