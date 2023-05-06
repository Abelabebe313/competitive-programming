class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if x < y:
                heapq.heappush(stones,(x-y))
        stones.append(0)
        return abs(stones[0])