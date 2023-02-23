class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setofchar = set()
        l = 0
        result = 0
        
        for r in range(len(s)):
            while s[r] in setofchar:
                setofchar.remove(s[l])
                l += 1
            setofchar.add(s[r])
            result = max(result,r - l +1)
        return result