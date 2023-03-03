class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles.sort()
        # total = sum(piles)

        left = 1
        right = max(piles)
        # mid = 0
        result = right
        while left <= right:
            mid = (left+right)//2

            total = 0
            for p in piles:
                total += math.ceil(p/mid)

            if total <= h:
                result = mid
                right = mid - 1
            else:
                left = mid+1
        return result