class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxi = 0
        total = 0
        window = defaultdict(int)
        
        for right in range(len(s)):
            total += 1
            window[s[right]] += 1
            maximum = max(window.values())
            
            while total - maximum > k:
                maxi = max(maxi, total - 1)
                total -= 1
                window[s[left]] -= 1
                maximum = max(window.values())
                left += 1
        maxi = max(maxi,total)
        return maxi
        