class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        maxHight = float(-inf)
        
        for i in range(len(gain)):
            prefix.append(prefix[-1] + gain[i])
        for r in range(len(prefix)):
            maxHight = max(maxHight,prefix[r])
            
        return maxHight