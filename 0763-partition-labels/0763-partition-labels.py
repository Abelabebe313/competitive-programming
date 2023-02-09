class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccur = {}
        for i,c in enumerate(s):
            lastOccur[c] = i
        
        ans = []
        start = 0
        right = 0
        for i in range(len(s)):
            if lastOccur[s[i]] >= right:
                right = lastOccur[s[i]]
             
            if i == right:
                ans.append(i+1 - start)
                start = i + 1
                # left = 0
            
        return ans
        