class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        pq = []
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if len(pq) < ladders:
                    heapq.heappush(pq, diff)
                else:
                    prev_diff = diff
                    if pq and pq[0] < diff:
                        prev_diff = heappop(pq)
                        heappush(pq,diff)
                    if (bricks-prev_diff) >= 0:
                        bricks -= prev_diff
                    else:
                        return i-1
        return i

