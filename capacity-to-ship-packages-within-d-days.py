class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            count = 0
            total = 0
            for w in weights:
                if (w + total) > mid:
                    count += 1
                    total = 0
                total += w

            if total:
                count += 1
            
            if count <= days:
                ans = min(ans, mid)
                right = mid -1
            else:
                left = mid + 1
        return ans